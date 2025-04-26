import time
from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then
from pages.base_page import Page
# from pages.side_nav_ui import SideNavMenu

# add locator for add project
BUTTON_ADD_PROJECTS = (By.CSS_SELECTOR, "a[href='/add-a-project']")
SETTINGS_PAGE_DYNAMIC_TITLE_LOCATOR = (By.CLASS_NAME, 'name-prifile-setting')
EXPECTED_USER_NAME = 'test+alexander+careerist'


@when('Click on Add a project')
def click_on_add_project(context):
    context.app.settings_page.verify_settings_page_fully_loaded(SETTINGS_PAGE_DYNAMIC_TITLE_LOCATOR, EXPECTED_USER_NAME)

    context.app.settings_page.click_on_add_project(*BUTTON_ADD_PROJECTS)
