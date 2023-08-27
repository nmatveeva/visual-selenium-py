from tests.conftest import validate_window_layout_level, validate_window_full_page, validate_element
from pages.dynamic_content import DynamicContentPage
from pages.large_deep_dom import LargeDeepDom
from pages.notif_msg import NotificationMessagePage


def test_match_level_layout(driver, eyes):
    dynamic_content_page = DynamicContentPage(driver)
    dynamic_content_page.load()
    validate_window_layout_level(driver, eyes)


def test_full_page_with_large_dom(driver, eyes):
    large_deep_dom_page = LargeDeepDom(driver)
    large_deep_dom_page.load()
    validate_window_full_page(driver, eyes)


def test_element_present(driver, eyes):
    notif_msg_page = NotificationMessagePage(driver)
    notif_msg_page.load()
    notif_msg_page.load_new_msg()
    notification = driver.find_element(*notif_msg_page.NOTIF_MSG)
    validate_element(driver, eyes, notification)
