#!/usr/bin/env python3

from matplotlib.pyplot import subplots, show
from wordcloud import WordCloud

from lib import get_data


class Visualiser:
    def __init__(self):
        self.loans = get_data()
        self.loans["Unique title"] = [
            "".join([i for i in title if i != "-" and not i.isdigit()]).rstrip().lower()
            for title in self.loans["Loan title"]
        ]
        self.loans["Unique title"] = [
            a[:-5]
            if (a[-5:] == " loan" and a[:-5] in self.loans["Unique title"].values)
            else a
            for a in self.loans["Unique title"]
        ]
        self.live_loans = self.loans[
            self.loans["Loan status"].isin(["Live", "Late", "Processing"])
        ]
        self.i = 0
        self.total_remaining_principal = self.live_loans["Principal remaining"].sum()

    def new_plot(self, title, print_title=True):
        fig, ax = subplots(num=f"{self.i} {title}")
        self.i += 1
        if print_title:
            ax.set_title(title)
        return fig, ax

    def pie_chart(self, data, column, title_=""):
        fig, ax_ = self.new_plot(title_)
        getattr(self, data)[column].value_counts().plot.pie(ax=ax_)
        ax_.set_ylabel("")

    def risk_distribution(self):
        risk_principal = []
        risk_names = ("A+", "A ", "B ", "C ", "D ", "E ", "nan")
        for risk in risk_names:  # nan not working
            risk_principal.append(
                sum([a[6] for a in vis.live_loans.values if a[4] == risk])
            )
        return risk_names, risk_principal

    def risk_distribution_pie(self):
        fig, ax = self.new_plot("Distribution of money over risk bands")
        risk_names, risk_principal = self.risk_distribution()
        ax.pie(risk_principal, labels=risk_names)

    def risk_distribution_bar(self):
        fig, ax = self.new_plot("Distribution of money over risk bands")
        risk_names, risk_principal = self.risk_distribution()
        ax.bar(range(len(risk_principal)), risk_principal, tick_label=risk_names)
        ax.set_xlabel("Risk band")
        ax.set_ylabel("Money / £")

    def titles_cloud(self):
        fig, ax = self.new_plot("Titles", print_title=False)
        wordcloud = WordCloud(
            background_color="white", scale=4, width=960, height=540
        ).fit_words(vis.loans["Unique title"].value_counts())
        ax.imshow(wordcloud, interpolation="bilinear")
        ax.axis("off")


if __name__ == "__main__":
    vis = Visualiser()
    # vis.pie_chart("live_loans", "Sector", "Sector distribution of live loans")
    # vis.pie_chart("loans", "Loan status", "Loan status distribution")
    # vis.risk_distribution_pie()
    vis.titles_cloud()

    show()
