#!/usr/bin/env python3

import pandas
import matplotlib.pyplot as plt
from argparse import ArgumentParser


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("filename", type=str, help="Name of income forecast CSV file")
    args = parser.parse_args()
    data = pandas.read_csv(args.filename)
    data["profit"] = data["pay_interest"] - data["lender_fee"]
    data["income"] = data["pay_principal"] + data["profit"]
    data["profit_cumulative"] = data["profit"].cumsum()
    data["income_cumulative"] = data["income"].cumsum()

    print(data["due_date"][0])

    # plt.scatter(data["due_date"], data["income_cumulative"])
    # plt.show()
