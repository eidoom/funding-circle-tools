#!/usr/bin/env python
# coding=utf-8

from graphing import do_graphing
from tracking import do_tracking


def quick(verbose):
    print("Scraping...")
    do_tracking(verbose)

    print("Plotting...")
    do_graphing(verbose)

    print("Script complete.")


def main():
    verbose = False
    do_tracking(verbose)


if __name__ == "__main__":
    main()
