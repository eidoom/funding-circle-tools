#!/usr/bin/env python
# coding=utf-8

from argparse import ArgumentParser
from configparser import ConfigParser
from os import path
from platform import system as operating_system

SETTINGS_FILE = "settings.cfg"
DATA_FILE = "scrape_info.csv"


class Configuration:
    def __init__(self):
        self.os_name = operating_system()
        self.current_directory = path.dirname(path.realpath(__file__))

        self.show_available_funds = True
        self.show_figure = True
        self.save_figure = True

        self.days_to_show = 49

        config = ConfigParser()
        config.read(SETTINGS_FILE)

        login = config["login"]

        self.username = login["username"]
        self.password = login["password"]

        self.school = login["school"]
        self.friend = login["friend"]
        self.where = login["where"]

        program = config["program"]

        self.chrome_driver_directory = program["chrome_driver_directory"]


class QuietArgument:
    def __init__(self):
        parser = ArgumentParser()
        parser.add_argument("-q", "--quiet", action="store_true",
                            help="Turn off verbose output")
        args = parser.parse_args()
        self.verbose = not args.quiet
