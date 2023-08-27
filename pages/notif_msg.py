"""
This module contains NotificationMessagePage,
the page object for the notification message page.
"""
from selenium.webdriver.common.by import By


class NotificationMessagePage:

    URL = "https://the-internet.herokuapp.com/notification_message_rendered"
    CLICK_HERE_LINK = (By.LINK_TEXT, "Click here")
    NOTIF_MSG = (By.ID, "flash-messages")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def load_new_msg(self):
        msg_link = self.browser.find_element(*self.CLICK_HERE_LINK)
        msg_link.click()
