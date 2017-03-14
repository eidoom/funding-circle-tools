#!/usr/bin/env python
# coding=utf-8

from configparser import ConfigParser
from os.path import isfile
from sys import exit

from configuration import SETTINGS_FILE, DATA_FILE


def main():
    if isfile(SETTINGS_FILE) or isfile(DATA_FILE):
        if input("Warning: will overwrite existing files - proceed? (yes) ") != "yes":
            exit()

    config = ConfigParser()

    config["login"] = {"username": "",
                       "password": "",
                       "school": "",
                       "friend": "",
                       "where": ""}

    config["program"] = {"chrome_driver_directory": ""}

    with open(SETTINGS_FILE, "w+") as config_file:
        config.write(config_file)

    with open(DATA_FILE, "w+") as data_file:
        data_file.write('"when","available funds","gross yield","annualised return",'
                        '"estimated return","earnings","fees","losses","net earnings"\n')


if __name__ == "__main__":
    main()
