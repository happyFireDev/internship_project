import time

from pages.base_page import Page

class SettingsPage(Page):


    def verify_settings_page_fully_loaded(self, locator, expected_text):

        # Wait until the text is present
        self.wait_until_element_text_is_present(locator, expected_text)


    def click_on_add_project(self, *locator):
        # time.sleep(2)
        self.wait_until_clickable_click(*locator)


