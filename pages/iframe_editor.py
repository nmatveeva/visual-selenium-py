"""
This module contains IFrameEditorPage,
the page object for the iFrame Editor page.
"""
from selenium.webdriver.common.by import By


class IFrameEditorPage:

    URL = "https://the-internet.herokuapp.com/tinymce"
    EDITOR = (By.TAG_NAME, "iframe")
    EDITOR_TEXT_AREA = (By.ID, "tinymce")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)
