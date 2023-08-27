import json
import os
from datetime import datetime as dt
import pytest
from applitools.common import MatchLevel
from applitools.selenium import Eyes
from selenium import webdriver

from constants import BASE_DIR
from pages.dynamic_content import DynamicContentPage

APP_NAME = "the-internet"
APP_UNDER_TEST = DynamicContentPage.URL


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config: pytest.Config) -> None:
    if not os.path.exists(f'{BASE_DIR + "reports"}'):
        os.makedirs(f'{BASE_DIR}/reports')
    config.option.htmlpath = (f'{BASE_DIR}reports/'
                              + dt.now().strftime('%Y-%m-%d_%H-%M-%S',)
                              + '_report.html')


@pytest.fixture(scope='session')
def config():

    with open('config.json') as config_file:
        config = json.load(config_file)

    return config


@pytest.fixture(scope="function")
def driver(config):
    # Init the Webdriver instance
    if config['browser'] == 'Chrome':
        driver = webdriver.Chrome()
    elif config['browser'] == 'Firefox':
        driver = webdriver.Firefox()
    elif config['browser'] == 'Headless Chrome':
        opts = webdriver.ChromeOptions()
        opts.add_argument('headless')
        driver = webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait for elements to appear
    driver.implicitly_wait(config['implicit_wait'])

    driver.get(APP_UNDER_TEST)
    yield driver
    driver.quit()


def initialize_eyes(config):
    eyes = Eyes()
    eyes.api_key = config["APPLITOOLS_API_KEY"]
    return eyes


@pytest.fixture(scope="function")
def eyes(config):
    eyes = initialize_eyes(config)
    yield eyes


def open_eyes(driver, eyes):
    eyes.open(driver, APP_NAME, test_name=get_test_name())


def get_test_name():
    import inspect
    return inspect.stack()[3].function


def close_eyes(eyes):
    eyes.close()


def validate_window(driver, eyes, tag=None):
    open_eyes(driver, eyes)
    eyes.match_level = MatchLevel.LAYOUT
    eyes.check_window(tag=tag)
    close_eyes(eyes)
