#!/usr/bin/env python
# coding=utf-8

from csv import reader
from datetime import datetime, timedelta

from matplotlib.pyplot import subplots, get_current_fig_manager, show

from configuration import Configuration, QuietArgument, DATA_FILE


def selector(when, input_values, days_to_show):
    latest_time = when[-1]

    interval_time = timedelta(days=days_to_show)

    search_start_time = latest_time - interval_time

    nearest_start_time = next(
        time for time in when if time > search_start_time)

    start_time_index = when.index(nearest_start_time)

    reduced_when = when[start_time_index:]

    reduced_values = input_values[start_time_index:]

    return reduced_when, reduced_values


def sub_plotter(ax, when, all_values, value_titles, plot_title,
                y_label, days_to_show=None, zoom=False, fixed=False):
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    ax.set_title(plot_title)
    ax.set_ylabel(y_label)

    for plot_title in value_titles:
        input_values = all_values[plot_title]
        if days_to_show:
            when2, input2 = selector(when, input_values, days_to_show)
        else:
            when2 = when
            input2 = input_values
        ax.plot(when2, input2, label=plot_title)

    adjustment = 1  # %

    if zoom:
        range1 = all_values[value_titles[0]]
        range2 = selector(when, range1, days_to_show)[1] if days_to_show else range1
        ax.set_ylim(min(range2) * (1 - adjustment / 100), max(range2) * (1 + adjustment / 100))

    if len(value_titles) > 1:
        ax.legend(loc="upper left" if fixed else "best")


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
        good_debt = round(100 * all_values["net earnings"][-1] / all_values["earnings"][-1], 1)
        print("  Good debt: " + str(good_debt) + "%")

    columns = 3 if config.middle_column else 2
    last = columns - 1
    fig, (axs_top, axs_bottom) = subplots(nrows=2, ncols=columns)

    pound_label = "£"
    percentage_label = "%"

    top_value_labels = ("net earnings", "earnings", "fees", "losses")
    top_plot_title = "Earnings Overview"

    sub_plotter(axs_top[0], when, all_values, top_value_labels, f"{top_plot_title} - all time",
                pound_label, fixed=True)
    if config.middle_column:
        sub_plotter(axs_top[1], when, all_values, top_value_labels,
                    f"{top_plot_title} - last {config.middle_label}", pound_label,
                    config.middle_period, zoom=True)
    sub_plotter(axs_top[last], when, all_values, ("net earnings",),
                f"Net Earnings - last {config.end_label}", pound_label,
                config.end_period)

    bottom_value_labels = ("annualised return", "gross yield", "estimated losses",
                           "returns fees", "estimated return")
    bottom_plot_title = "Returns Overview"

    sub_plotter(axs_bottom[0], when, all_values, bottom_value_labels, bottom_plot_title,
                percentage_label, fixed=True)
    if config.middle_column:
        sub_plotter(axs_bottom[1], when, all_values, bottom_value_labels,
                    f"{bottom_plot_title} - last {config.middle_label}", percentage_label,
                    config.middle_period, zoom=True)
    if config.plot_available_funds:
        sub_plotter(axs_bottom[last], when, all_values, ("available funds",),
                    "Available Funds", pound_label, config.end_period)
    else:
        sub_plotter(axs_bottom[last], when, all_values, ("annualised return",),
                    f"Net Return - last {config.end_label}", percentage_label,
                    config.end_period)

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
