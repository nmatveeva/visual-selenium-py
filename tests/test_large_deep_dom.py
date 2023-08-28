import pytest

from pages.large_deep_dom import LargeDeepDom
from tests.conftest import APP_NAME


@pytest.fixture(scope='module')
def setup_suite(manager, driver):
    manager.set_batch('Large & Deep DOM')
    manager.set_app_name(APP_NAME)
    LargeDeepDom(manager.driver).load()


def test_full_page_with_large_dom(manager):
    manager.validate_window(full_page=True)
