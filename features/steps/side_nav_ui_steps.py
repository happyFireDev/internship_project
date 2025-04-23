import time
from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then
from pages.base_page import Page

SETTINGS_PAGE_LINK = (By.XPATH, "//a[contains(., 'Settings')]")

@then('Click on the settings option')
def click_settings_link_in_side_name(context):
    context.app.side_nav_ui.click_settings_link_in_side_name(*SETTINGS_PAGE_LINK)

