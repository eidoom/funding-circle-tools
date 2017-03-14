#!/usr/bin/env python
# coding=utf-8

from csv import reader
from datetime import datetime, timedelta

from matplotlib.pyplot import subplots, get_current_fig_manager, show

from configuration import Configuration, QuietArgument, DATA_FILE


def selector(config, when, input_values):
    latest_time = when[-1]

    interval_time = timedelta(days=config.days_to_show)

    search_start_time = latest_time - interval_time

    nearest_start_time = next(
        time for time in when if time > search_start_time)

    start_time_index = when.index(nearest_start_time)

    reduced_when = when[start_time_index:]

    reduced_values = input_values[start_time_index:]

    return reduced_when, reduced_values


def sub_plotter(config, ax, when, all_values, value_titles, plot_title,
                y_label, reduced_time):
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    ax.set_title(plot_title)
    ax.set_ylabel(y_label)

    for plot_title in value_titles:
        input_values = all_values[plot_title]
        if reduced_time:
            when2, input2 = selector(config, when, input_values)
        else:
            when2 = when
            input2 = input_values
        ax.plot(when2, input2, label=plot_title)

    if len(value_titles) > 1:
        ax.legend(loc="upper left")


def generate_graph(config, data):
    titles = data.pop(0)[1:]

    if not data[-1]:
        data = data[:-1]

    when = [datetime.strptime(row.pop(0), "%Y-%m-%d %H:%M:%S.%f")
            for row in data]

    all_values = {title: [float(row[n].replace(",", "")) for row in data]
                  for n, title in enumerate(titles)}

    all_values["estimated losses"] = [
        a - b - 1 for a, b in
        zip(all_values["gross yield"], all_values["estimated return"])]

    all_values["returns fees"] = [1] * len(when)

    if config.show_available_funds:
        print("  Available funds: £" + str(all_values["available funds"][-1]))

    fig, ((ax1, ax2), (ax3, ax4)) = subplots(2, 2)

    sub_plotter(config, ax1, when, all_values,
                ("net earnings", "earnings", "fees", "losses"),
                "Earnings Overview", "£", False)
    sub_plotter(config, ax2, when, all_values, ("net earnings",),
                "Net Earnings", "£", True)
    sub_plotter(config, ax3, when, all_values,
                ("annualised return", "gross yield", "estimated losses",
                 "returns fees", "estimated return"), "Returns Overview",
                "%", False)
    sub_plotter(config, ax4, when, all_values, ("annualised return",),
                "Net Return", "%", True)

    fig.set_tight_layout("tight")

    return fig


def do_graphing(verbose):
    config = Configuration()

    if verbose:
        print("  Plotting results...")

    with open(DATA_FILE, "r") as csv_file:
        csv_data = list(reader(csv_file, delimiter=","))

    fig = generate_graph(config, csv_data)

    fig_manager = get_current_fig_manager()
    fig_manager.window.showMaximized()

    if config.show_figure:
        show()

    if config.save_figure:
        if config.os_name == "Windows":
            fig.savefig("graph.pdf")
        else:
            fig.savefig("{}/graph.pdf".format(config.current_directory))

    if verbose:
        print("  Python plotting script complete.")


def main():
    args = QuietArgument()
    do_graphing(args.verbose)


if __name__ == "__main__":
    main()
