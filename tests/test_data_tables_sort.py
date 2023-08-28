import pytest

from pages.data_tables import DataTablesPage
from tests.conftest import APP_NAME


@pytest.fixture(scope='module')
def setup_suite(manager, driver):
    manager.set_batch('Data Tables Sort')
    manager.set_app_name(APP_NAME)
    DataTablesPage(manager.driver).load()


def test_by_first_name(manager):
    data_tables_page = DataTablesPage(manager.driver)
    data_tables_page.sort_by_first_name()
    manager.validate_window(tag='by_first_name')


def test_by_last_name(manager):
    data_tables_page = DataTablesPage(manager.driver)
    data_tables_page.sort_by_last_name()
    manager.validate_window(tag='by_last_name')
