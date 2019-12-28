from pandas import read_csv
from argparse import ArgumentParser


# csv -> pandas.dataframe
def get_data():
    parser = ArgumentParser()
    parser.add_argument("filename", type=str, help="Name of income forecast CSV file")
    args = parser.parse_args()
    return read_csv(args.filename)


if __name__ == "__main__":
    exit("This file is not for running!")
