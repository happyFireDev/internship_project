import time
from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then
from pages.base_page import Page


EMAIL_ADDRESS_FIELD = (By.CSS_SELECTOR, '#email-2')
USER_EMAIL_ADDRESS = ''
USER_PASSWORD_FIELD = (By.NAME, "Password")
USER_PASSWORD = ''
LOGIN_PAGE_SLUG = 'sign-in'
LOGIN_BUTTON = (By.CSS_SELECTOR, ".login-button")




@given('Open the login page')
def open_logged_in_page_via_url(context):
    context.app.sign_in_page.open_logged_in_page_via_url(LOGIN_PAGE_SLUG)

@when('Enter email')
def enter_email(context):
    context.app.sign_in_page.enter_user_email(USER_EMAIL_ADDRESS,*EMAIL_ADDRESS_FIELD)

@when('Enter password')
def enter_password(context):
    context.app.sign_in_page.enter_user_password(USER_PASSWORD,*USER_PASSWORD_FIELD)

@when('Click login button')
def click_login_button(context):
    context.app.sign_in_page.click_login_button(*LOGIN_BUTTON)

