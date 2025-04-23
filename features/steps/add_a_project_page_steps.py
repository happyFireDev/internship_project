import time
from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then
from webdriver_manager.core import driver

from pages.base_page import Page

# LOCATORS
ADD_A_PROJECT_FULL_URL_PATH = 'https://soft.reelly.io/add-a-project'

INPUT_FIELD_YOUR_NAME = (By.ID, "Your-name")
INPUT_FIELD_YOUR_NAME_STRING = "Sam Hill"

INPUT_FIELD_YOUR_COMPANY_NAME = (By.ID, "Your-company-name")
INPUT_FIELD_YOUR_COMPANY_NAM_STRING = "test"

INPUT_FIELD_YOUR_ROLE = (By.ID, "Role")
INPUT_FIELD_YOUR_ROLE_STRING = "Tester"

INPUT_FIELD_AGE_COMPANY = (By.ID, "Age-of-the-company")
INPUT_FIELD_AGE_COMPANY_STRING = "100"

BUTTON_APPLICATION = (By.XPATH, "//input[@value='Send an application']")


@then('Verify the right page opens')
def verify_add_a_project_page_opens(context):
    context.app.add_a_project_page.verify_add_a_project_page_opens(ADD_A_PROJECT_FULL_URL_PATH)


@then('Add some test information to the input fields')
def add_test_info_to_fields(context):
    context.app.add_a_project_page.add_test_info_to_fields(INPUT_FIELD_YOUR_NAME_STRING, *INPUT_FIELD_YOUR_NAME)

    context.app.add_a_project_page.add_test_info_to_fields(INPUT_FIELD_YOUR_COMPANY_NAM_STRING, *INPUT_FIELD_YOUR_COMPANY_NAME)

    context.app.add_a_project_page.add_test_info_to_fields(INPUT_FIELD_YOUR_ROLE_STRING,*INPUT_FIELD_YOUR_ROLE)

    context.app.add_a_project_page.add_test_info_to_fields(INPUT_FIELD_AGE_COMPANY_STRING,*INPUT_FIELD_AGE_COMPANY)



@then('Verify the correct information is present in the input fields')
def verify_text_is_present_on_add_a_project(context):

    context.app.add_a_project_page.verify_text_is_present_on_add_a_project(INPUT_FIELD_YOUR_NAME_STRING, *INPUT_FIELD_YOUR_NAME)

    context.app.add_a_project_page.verify_text_is_present_on_add_a_project(INPUT_FIELD_YOUR_COMPANY_NAM_STRING, *INPUT_FIELD_YOUR_COMPANY_NAME)

    context.app.add_a_project_page.verify_text_is_present_on_add_a_project(INPUT_FIELD_YOUR_ROLE_STRING,*INPUT_FIELD_YOUR_ROLE)

    context.app.add_a_project_page.verify_text_is_present_on_add_a_project(INPUT_FIELD_AGE_COMPANY_STRING,*INPUT_FIELD_AGE_COMPANY)

@then('Verify the “Send an application” button is available and clickable')
def verify_application_button_is_available(context):
    context.app.add_a_project_page.verify_application_button_is_available(*BUTTON_APPLICATION)

    sleep(5)