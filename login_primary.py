#!/usr/bin/env python
# coding=utf-8

from configuration import Configuration, QuietArgument
from scrape_core import log_in


def main():
    args = QuietArgument()
    config = Configuration()

    driver = log_in(config, args.verbose)

    available_funds = driver.find_element_by_class_name("header__user-funds").text[17:]

    # driver.get("https://www.fundingcircle.com/lend/loan-requests/sort/avg_rate/")
    driver.get("https://www.fundingcircle.com/lend/loan-requests")
    assert "Funding Circle - The Peer to Peer lending marketplace for small business loans" \
           == driver.title

    driver.find_element_by_link_text("/lend/loan-requests/sort/avg_rate/").click().click()


if __name__ == "__main__":
    main()
