#!/usr/bin/env python
# coding=utf-8

from scrape_core import log_in
from configuration import Configuration, QuietArgument


def main():
    args = QuietArgument()
    config = Configuration()

    driver = log_in(config, args.verbose)

    available_funds = driver.find_element_by_class_name("header__user-funds").text[17:]

    driver.get("https://www.fundingcircle.com/secondary-market")
    assert "Funding Circle" == driver.title

    max_price = driver.find_element_by_id("loan_part_paginator_sale_price_max")
    max_price.send_keys(available_funds)

    exclude_previous_businesses = driver.find_element_by_id(
        "loan_part_paginator_exclude_businesses_funded")
    exclude_previous_businesses.click()

    risk_band_a = driver.find_element_by_id("loan_part_paginator_credit_band_name_a")
    risk_band_b = driver.find_element_by_id("loan_part_paginator_credit_band_name_b")
    risk_band_c = driver.find_element_by_id("loan_part_paginator_credit_band_name_c")
    risk_band_d = driver.find_element_by_id("loan_part_paginator_credit_band_name_d")
    risk_band_e = driver.find_element_by_id("loan_part_paginator_credit_band_name_e")

    sort_rates_available = driver.find_element_by_id("sort_buyer_rate")
    sort_rates_available.click()


    # show_advanced_filters = driver.find_element_by_class_name("hidden down-icon prev")
    # show_advanced_filters.click()

    # max_premium = driver.find_element_by_id("loan_part_paginator_mark_up_percent_max")
    # max_premium.click()
    # max_premium.send_keys(Keys.ARROW_UP)
    # max_premium.send_keys(Keys.ARROW_UP)
    # max_premium.send_keys(Keys.ARROW_UP)
    # max_premium.send_keys(Keys.ARROW_UP)
    # max_premium.send_keys(Keys.RETURN)


if __name__ == "__main__":
    main()
