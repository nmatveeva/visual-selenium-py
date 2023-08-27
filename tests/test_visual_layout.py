from tests.conftest import validate_window_layout_level, validate_window_full_page
from pages.dynamic_content import DynamicContentPage
from pages.large_deep_dom import LargeDeepDom


def test_match_level_layout(driver, eyes):
    dynamic_content_page = DynamicContentPage(driver)
    dynamic_content_page.load()
    validate_window_layout_level(driver, eyes)


def test_full_page_with_large_dom(driver, eyes):
    large_deep_dom_page = LargeDeepDom(driver)
    large_deep_dom_page.load()
    validate_window_full_page(driver, eyes)
