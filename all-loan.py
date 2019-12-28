#!/usr/bin/env python3

from lib import get_data

from matplotlib.pyplot import subplots, show


class Visualiser:
    def __init__(self):
        self.loans = get_data()
        self.live_loans = self.loans[
            self.loans["Loan status"].isin(["Live", "Late", "Processing"])
        ]
        self.i = 0
        self.total_remaining_principal = self.live_loans["Principal remaining"].sum()

    def new_plot(self, title):
        fig, ax = subplots(num=f"{self.i} {title}")
        self.i += 1
        return fig, ax

    def pie_chart(self, data, column, title_=""):
        fig, ax_ = self.new_plot(title_)
        getattr(self, data)[column].value_counts().plot.pie(ax=ax_, title=title_)
        ax_.set_ylabel("")

    def risk_distribution(self):
        title = "Distribution of money over risk bands"
        fig, ax = self.new_plot(title)
        risk_principal = []
        risk_names = ("A+", "A ", "B ", "C ", "D ", "E ", "nan")
        for risk in risk_names:  # nan not working
            risk_principal.append(
                sum([a[6] for a in vis.live_loans.values if a[4] == risk])
            )
        ax.bar(range(len(risk_principal)), risk_principal, tick_label=risk_names)
        ax.set_xlabel("Risk band")
        ax.set_ylabel("Money / £")
        ax.set_title(title)


if __name__ == "__main__":
    vis = Visualiser()
    vis.pie_chart("live_loans", "Sector", "Sector distribution of live loans")
    # vis.pie_chart("loans", "Loan status", "Loan status distribution")
    vis.risk_distribution()

    # show()
