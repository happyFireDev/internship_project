from pages.base_page import Page

class SideNavMenu(Page):

    def verify_user_is_fully_logged_in_by_checking_company_name(self, locator, expected_text):
        element = self.wait_until_element_text_is_present(locator, expected_text)
        print(f"✅ Verified user login with text: {element.text.strip()}")

    def click_settings_link_in_side_name(self, *locator):
        self.wait_until_clickable_click(*locator)
