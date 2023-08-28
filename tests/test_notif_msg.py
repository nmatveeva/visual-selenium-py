import pytest

from pages.notif_msg import NotificationMessagePage
from tests.conftest import APP_NAME


@pytest.fixture(scope='module')
def setup_suite(manager, driver):
    manager.set_batch('Notification Message')
    manager.set_app_name(APP_NAME)
    NotificationMessagePage(manager.driver).load()


def test_element_present(manager):
    notif_msg_page = NotificationMessagePage(manager.driver)
    notif_msg_page.load_new_msg()
    notification = manager.driver.find_element(*notif_msg_page.NOTIF_MSG)
    manager.validate_element(notification)
