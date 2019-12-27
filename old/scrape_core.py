#!/usr/bin/env python
# coding=utf-8

from sys import exit

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def log_in(config, verbose):
    if verbose:
        print("  Starting web browser...")

    if config.os_name == "Windows":
        chrome_driver_path = \
            f"{config.chrome_driver_directory}\chromedriver.exe"
        driver = webdriver.Chrome(chrome_driver_path)
    else:
        driver = webdriver.Chrome()

    if verbose:
        print("  Opening up Funding Circle...")

    # driver.maximize_window()

    driver.get("https://www.fundingcircle.com/login")

    assert "Funding Circle - Apply for a business loan or register as an " \
           "investor" == driver.title

    if verbose:
        print("  Logging into Funding Circle...")

    username_field = driver.find_element_by_xpath("//input[@id='user_username']")
    username_field.send_keys(config.username)

    password_field = driver.find_element_by_xpath("//input[@id='user_password']")
    password_field.send_keys(config.password)

    password_field.send_keys(Keys.RETURN)

    assert "Funding Circle - The Peer to Peer lending marketplace for small " \
            "business loans" == driver.title

    security_question = driver.find_element_by_class_name(
        "input__label--above").text
    security_answer = driver.find_element_by_id("user_input")

    if security_question == \
            "What school did you attend when you were 10 years old?":
        security_answer.send_keys(config.school)
    elif security_question == \
            "What was the name of your best friend at school?":
        security_answer.send_keys(config.friend)
    elif security_question == "Where did you grow up?":
        security_answer.send_keys(config.where)
    else:
        exit("Error: Security Question changed?")

    security_answer.send_keys(Keys.RETURN)

    assert "My Summary - Funding Circle" == driver.title

    if verbose:
        print("  Successfully logged into Funding Circle.")

    return driver


if __name__ == "__main__":
    exit()
