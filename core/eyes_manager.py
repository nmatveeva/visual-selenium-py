"""
This module contains the EyesManager
"""
import json

import applitools.common
from applitools.common import MatchLevel
from applitools.selenium import Eyes

from constants import BASE_DIR


class EyesManager:

    def __init__(self, driver):
        self.app_name = None
        self.driver = driver
        self.eyes = self.initialize_eyes()

    @staticmethod
    def initialize_eyes():
        with open(f'{BASE_DIR}config.json') as config_file:
            config = json.load(config_file)
        eyes = Eyes()
        eyes.api_key = config["APPLITOOLS_API_KEY"]
        return eyes

    def set_app_name(self, app_name):
        self.app_name = app_name

    def set_batch(self, batch_name):
        if batch_name:
            batch_info = applitools.common.BatchInfo(batch_name)
            self.eyes.batch = batch_info

    def validate_window(self, tag=None, full_page=False, match_lvl=MatchLevel.LAYOUT):
        self.eyes.match_level = match_lvl
        if full_page:
            self.eyes.force_full_page_screenshot = True

        self.eyes.check_window(tag=tag)

    def validate_element(self, element, tag=None, match_lvl=MatchLevel.LAYOUT):
        self.eyes.match_level = match_lvl
        self.eyes.check_region(element, tag=tag)

    def validate_frame(self, frame_reference, region, tag=None):
        self.eyes.check_region_in_frame(frame_reference, region, tag=None)

    def open_eyes(self, test_name):
        self.eyes.open(self.driver, self.app_name, test_name=test_name)

    def close_eyes(self):
        self.eyes.close()
