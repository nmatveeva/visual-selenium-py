import json
import os
from datetime import datetime as dt
import pytest
from selenium import webdriver

from constants import BASE_DIR
from core.eyes_manager import EyesManager

APP_NAME = "the-internet.herokuapp.com"


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config: pytest.Config) -> None:
    if not os.path.exists(f'{BASE_DIR + "reports"}'):
        os.makedirs(f'{BASE_DIR}/reports')
    config.option.htmlpath = (f'{BASE_DIR}reports/'
                              + dt.now().strftime('%Y-%m-%d_%H-%M-%S',)
                              + '_report.html')


@pytest.fixture(scope='session')
def config():
    # Read the config file
    with open(f'{BASE_DIR}config.json') as config_file:
        config = json.load(config_file)

    return config


@pytest.fixture(scope="module")
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

    # Maximize the browser window
    driver.maximize_window()

    # Return the WebDriver instance for the setup
    yield driver

    # Quit the WebDriver instance for the cleanup
    driver.quit()


@pytest.fixture(scope="module")
def manager(driver):
    eyes_manager = EyesManager(driver)
    yield eyes_manager


@pytest.fixture(scope="function", autouse=True)
def setup_eyes(request, setup_suite, manager):
    test_name = request.function.__name__
    manager.open_eyes(test_name)
    yield setup_eyes
    manager.close_eyes()
