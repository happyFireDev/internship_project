import time
from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then
from pages.base_page import Page

SETTINGS_PAGE_LINK = (By.XPATH, "//a[contains(., 'Settings')]")
SETTINGS_PAGE_LINK_MOBILE = (By.CSS_SELECTOR, ".settings-link.w-inline-block")
SETTINGS_PAGE_LINK_NEW = (By.LINK_TEXT, "Settings")
LOGIN_SUCCESS_LOCATOR = (By.CLASS_NAME, 'name_text_account')
EXPECTED_LOGIN_TEXT = 'test+alexander+careerist'


@when('Click on the settings option')
def click_settings_link_in_side_name(context):

    if context.platform == 'mobile':
        context.app.side_nav_ui.click_settings_link_in_side_name(*SETTINGS_PAGE_LINK_MOBILE)
    else:
        # time.sleep(4)
        context.app.side_nav_ui.click_settings_link_in_side_name(*SETTINGS_PAGE_LINK_NEW)


@then("Verify user is fully logged in")
def verify_side_menu_loaded(context):

    if context.platform == 'mobile':
        time.sleep(2)
    else:
        (context.app.side_nav_ui.verify_user_is_fully_logged_in_by_checking_company_name(
            LOGIN_SUCCESS_LOCATOR, EXPECTED_LOGIN_TEXT)
         )



