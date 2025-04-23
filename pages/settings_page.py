from pages.base_page import Page

class SettingsPage(Page):


    def click_on_add_project(self, *locator):
        self.click(*locator)


