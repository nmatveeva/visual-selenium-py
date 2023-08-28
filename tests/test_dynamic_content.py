import pytest
from applitools.common import MatchLevel

from pages.dynamic_content import DynamicContentPage
from tests.conftest import APP_NAME


@pytest.fixture(scope='module')
def setup_suite(manager, driver):
    manager.set_batch('Dynamic Content')
    manager.set_app_name(APP_NAME)
    DynamicContentPage(manager.driver).load()


def test_match_level_layout(manager):
    manager.validate_window()


def test_match_level_strict(manager):
    dynamic_content_page = DynamicContentPage(manager.driver)
    dynamic_content_page.make_static()
    manager.validate_element(element=DynamicContentPage.STATIC_ELEM, match_lvl=MatchLevel.STRICT)
