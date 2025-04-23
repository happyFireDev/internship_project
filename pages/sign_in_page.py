from pages.base_page import Page

class SignInPage(Page):


    def open_logged_in_page_via_url(self, url_slug):
        self.open_logged_in_url(f'{self.base_logged_in_url}{url_slug}')


    def enter_user_email(self, text, *locator):
        # self.slow_type(text, *locator)
        self.input_text(text, *locator)

    def enter_user_password(self, text, *locator):
        # self.slow_type(text, *locator)
        self.input_text(text, *locator)

    def click_login_button(self, *locator):
        self.wait_until_clickable_click(*locator)
