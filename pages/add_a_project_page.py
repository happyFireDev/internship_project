from pages.base_page import Page
from selenium.webdriver.common.by import By

class AddAProjectPage(Page):


    def verify_add_a_project_page_opens(self, *locator):
        self.verify_url(*locator)


    def add_test_info_to_fields(self, text, *locator):
        self.input_text(text, *locator)


    def verify_text_is_present_on_add_a_project(self, expected_text, *locator):
        self.verify_text_enter_into_text_field(expected_text, *locator)


    def verify_application_button_is_available(self, *locator):
        self.wait_until_clickable(*locator)
