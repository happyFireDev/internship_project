from pages.base_page import Page
from pages.sign_in_page import SignInPage
from pages.side_nav_ui import SideNavMenu
from pages.settings_page import SettingsPage
from pages.add_a_project_page import AddAProjectPage

class Application:

    def __init__( self, driver):
        self.driver = driver

        self.add_a_project_page = AddAProjectPage(driver)
        self.base_page = Page(driver)
        self.sign_in_page = SignInPage(driver)
        self.side_nav_ui = SideNavMenu(driver)
        self.settings_page = SettingsPage(driver)


