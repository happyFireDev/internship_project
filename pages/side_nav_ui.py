from pages.base_page import Page

class SideNavMenu(Page):


    def click_settings_link_in_side_name(self, *locator):
        self.wait_until_clickable_click(*locator)
