from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep

def before_all(context):
    context.config.setup_logging()


def before_feature(context, feature):
    binary = FirefoxBinary('firefox')
    context.ff = webdriver.Firefox(firefox_binary=binary)


def after_feature(context, feature):
    sleep(5)
    context.ff.quit()


def after_all(context):
    sleep(2)

