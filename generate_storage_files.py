#!/usr/bin/env python
# coding=utf-8

from configparser import ConfigParser
from os.path import isfile
from platform import system as operating_system
from sys import exit

from configuration import SETTINGS_FILE, DATA_FILE


def main():
    print("Generating files for storing settings and scraped data...")
    os_name = operating_system()

    if isfile(SETTINGS_FILE) or isfile(DATA_FILE):
        if input("Warning: will overwrite existing files - proceed?") not in \
                ("y", "Y", "yes", "Yes"):
            exit()

    config = ConfigParser()

    print("Please input login details to populate settings file:")
    username = input("  Username: ")
    password = input("  Password: ")

    print("Now please input the answers to the security questions:")
    school = input("  What school did you attend when you were 10 years old? ")
    friend = input("  What was the name of your best friend at school? ")
    where = input("  Where did you grow up? ")

    if os_name == "Windows":
        chrome_driver_directory = input(
            "Please input the full path to the chromedriver installation directory: ")
    else:
        chrome_driver_directory = ""

    print("Generating settings file...")

    config["login"] = {"username": username,
                       "password": password,
                       "school": school,
                       "friend": friend,
                       "where": where}

    config["program"] = {"chrome_driver_directory": chrome_driver_directory}

    print("Writing settings file...")
    with open(SETTINGS_FILE, "w+") as config_file:
        config.write(config_file)

    print("Writing file to store scraped data...")
    with open(DATA_FILE, "w+") as data_file:
        data_file.write('"when","available funds","gross yield","annualised return",'
                        '"estimated return","earnings","fees","losses","net earnings"\n')

    print("Finished generating storage file.")


if __name__ == "__main__":
    main()
