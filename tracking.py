#!/usr/bin/env python
# coding=utf-8

from csv import writer
from datetime import datetime

from configuration import Configuration, QuietArgument, DATA_FILE
from scrape_core import log_in


def scrape_website(verbose, config):
    if verbose:
        print("  Scraping for information...")

    driver = log_in(config, verbose)

    available_funds = \
        driver.find_element_by_class_name("header__user-funds").text[17:]

    returns_summary = \
        driver.find_element_by_id("returns_summary").text.split("\n")

    # expand_buttons = driver.find_elements_by_xpath("//a[@href="#"]")
    # expand_buttons[0].click()
    # expand_buttons[1].click()

    earnings_summary = \
        driver.find_element_by_id("earnings_summary").text.split("\n")

    # funds_summary = driver.find_element_by_xpath("//div[@class="ng-scope"]")

    driver.quit()

    if verbose:
        print("  Completed scraping Funding Circle for information.")

    return available_funds, returns_summary, earnings_summary


def append_info_to_file(verbose, config, available_funds,
                        returns_summary, earnings_summary):
    if verbose:
        print("  Preparing information for writing to file...")

    when = datetime.now()

    row_info = [when,
                available_funds,
                returns_summary[1][:-1],
                returns_summary[3][:-1],
                returns_summary[6][:-1],
                earnings_summary[1][1:],
                earnings_summary[2].split("£")[1],
                # earnings_summary[3].split("£")[1],
                # earnings_summary[4].split("£")[0][-1:],
                # earnings_summary[4].split("£")[1],
                earnings_summary[4].split("£")[1],
                earnings_summary[5].split("£")[1]
                # earnings_summary[6].split("£")[1]
                # earnings_summary[8].split("£")[1],
                # earnings_summary[9].split("£")[1]
                # earnings_summary[10].split("£")[1],
                # earnings_summary[11].split("£")[1]
                ]

    if verbose:
        print("  Opening file for writing...")

    data_file = "{}/{}".format(config.current_directory, DATA_FILE)

    with open(data_file, "a") as file:
        if config.os_name == "Windows":
            data_write = writer(file, lineterminator="\n")
        else:
            data_write = writer(file)

        data_write.writerow(row_info)

    if verbose:
        print("  Information successfully written to file.")


def do_tracking(verbose):
    config = Configuration()

    available_funds, returns_summary, earnings_summary = \
        scrape_website(verbose, config)

    append_info_to_file(verbose, config, available_funds, returns_summary,
                        earnings_summary)

    if verbose:
        print("  Python Selenium scraping script complete.")


def main():
    args = QuietArgument()
    do_tracking(args.verbose)


if __name__ == "__main__":
    main()
