"""
This module contains DynamicContentPage,
the page object for the dynamic content page.
"""
from selenium.webdriver.common.by import By


class DynamicContentPage:

    URL = "https://the-internet.herokuapp.com/dynamic_content"
    CLICK_HERE_LINK = (By.LINK_TEXT, "click here")
    STATIC_ELEM = (By.XPATH, "//div[@id='content']/div[2]")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def make_static(self):
        msg_link = self.browser.find_element(*self.CLICK_HERE_LINK)
        msg_link.click()
