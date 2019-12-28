#!/usr/bin/env python3

from datetime import datetime

import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters

from lib import get_data

if __name__ == "__main__":
    data = get_data()

    data["due_date"] = [datetime.strptime(a, "%Y-%m-%d") for a in data["due_date"]]
    data = data.sort_values(by=["due_date", "loan_part_id"])
    data["profit"] = data["pay_interest"] - data["lender_fee"]
    data["income"] = data["pay_principal"] + data["profit"]
    data["profit_cumulative"] = data["profit"].cumsum()
    data["income_cumulative"] = data["income"].cumsum()

    register_matplotlib_converters()
    plt.plot(data["due_date"], data["income_cumulative"], label="Total")
    plt.plot(data["due_date"], data["profit_cumulative"], label="Interest")
    plt.xlabel("Date")
    plt.ylabel("Income / £")
    plt.legend()
    plt.title("Cumulative income forecast")
    plt.show()
