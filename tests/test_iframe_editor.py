import pytest

from pages.iframe_editor import IFrameEditorPage
from tests.conftest import APP_NAME


@pytest.fixture(scope='module')
def setup_suite(manager, driver):
    manager.set_batch('iFrame Editor')
    manager.set_app_name(APP_NAME)
    IFrameEditorPage(manager.driver).load()


def test_element_in_frame(manager):
    iframe_editor_page = IFrameEditorPage(manager)
    frame = manager.driver.find_element(*iframe_editor_page.EDITOR)
    manager.validate_frame(frame, iframe_editor_page.EDITOR_TEXT_AREA)
