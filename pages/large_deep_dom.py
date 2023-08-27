"""
This module contains LargeDeepDom,
the page object for the large & deep dom page.
"""


class LargeDeepDom:

    URL = "https://the-internet.herokuapp.com/large"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)
