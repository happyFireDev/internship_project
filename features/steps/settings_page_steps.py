import time
from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page
# from pages.side_nav_ui import SideNavMenu
from selenium.webdriver.support import expected_conditions as EC


# add locator for add project
BUTTON_ADD_PROJECTS = (By.CSS_SELECTOR, "a[href='/add-a-project']")
BUTTON_ADD_PROJECTS_MOBILE = (By.CSS_SELECTOR, 'a.page-setting-block.w-inline-block[href*="add-a-project"]')

SETTINGS_PAGE_DYNAMIC_TITLE_LOCATOR = (By.CLASS_NAME, 'name-prifile-setting')
EXPECTED_USER_NAME = 'test+alexander+careerist'

@when('Click on Add a project')
def click_on_add_project(context):
    context.app.settings_page.verify_settings_page_fully_loaded(SETTINGS_PAGE_DYNAMIC_TITLE_LOCATOR, EXPECTED_USER_NAME)

    if context.platform == 'mobile':
        # Wait for the mobile "Add a project" element to be present
        element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located(BUTTON_ADD_PROJECTS_MOBILE)
        )

        # Scroll into view
        context.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", element
        )
        time.sleep(0.5)  # Optional pause for rendering

        # Click it
        element.click()
        time.sleep(4)

    else:
        # For desktop, use the normal button
        context.app.settings_page.click_on_add_project(*BUTTON_ADD_PROJECTS)