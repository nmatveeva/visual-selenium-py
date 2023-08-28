"""
This module contains the DataTablesPage,
the page object for the data Tables page.
"""
from selenium.webdriver.common.by import By


class DataTablesPage:

    URL = "https://the-internet.herokuapp.com/tables"
    FIRST_NAME_COLUMN = (By.CSS_SELECTOR, "span[class='first-name']")
    LAST_NAME_COLUMN = (By.CSS_SELECTOR, "span[class='first-name']")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def sort_by_first_name(self):
        column = self.browser.find_element(*self.FIRST_NAME_COLUMN)
        column.click()

    def sort_by_last_name(self):
        column = self.browser.find_element(*self.LAST_NAME_COLUMN)
        column.click()
