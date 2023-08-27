"""
This module contains DynamicContentPage,
the page object for the dynamic content page.
"""


class DynamicContentPage:

    URL = "https://the-internet.herokuapp.com/dynamic_content"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)



