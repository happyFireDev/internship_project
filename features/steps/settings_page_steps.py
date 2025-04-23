import time
from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then
from pages.base_page import Page

# add locator for add project
BUTTON_ADD_PROJECTS = (By.CSS_SELECTOR, ".page-setting-block:nth-of-type(5)")

@then('Click on Add a project')
def click_on_add_project(context):
    context.app.settings_page.click_on_add_project(*BUTTON_ADD_PROJECTS)
