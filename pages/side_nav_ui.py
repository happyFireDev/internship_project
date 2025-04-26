from pages.base_page import Page

class SideNavMenu(Page):


    def verify_user_is_fully_logged_in_by_checking_company_name(self, *locator):
        self.wait_until_text_is_present(*locator)

    def click_settings_link_in_side_name(self, *locator):
        self.wait_until_clickable_click(*locator)
