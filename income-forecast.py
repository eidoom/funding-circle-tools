#!/usr/bin/env python3

import pandas
import matplotlib.pyplot as plt
from argparse import ArgumentParser


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("filename", type=str, help="Name of income forecast CSV file")
    args = parser.parse_args()
    data = pandas.read_csv(args.filename)
    due_date = data["due_date"]
    pay_principal = data["pay_principal"]

    plt.scatter(due_date, pay_principal)
    plt.show()
