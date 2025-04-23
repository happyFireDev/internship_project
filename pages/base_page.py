import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.reelly.ai/'
        self.base_logged_in_url = 'https://soft.reelly.io/'
        self.wait = WebDriverWait(self.driver, timeout=10)

    def open_url(self, url):
        self.driver.get(url)

    def open_logged_in_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)


    def verify_text_enter_into_text_field(self, custom_string, *field_locator):

        field_details = self.driver.find_element(*field_locator)

        entered_text = field_details.get_attribute("value")

        assert custom_string == entered_text, f'Expected "{custom_string}", but got "{entered_text}"'


    def slow_type(self, text, *locator, delay=0.1):
        self.wait.until(EC.presence_of_element_located(locator))
        element = self.driver.find_element(*locator)
        element.clear()
        for char in text:
            element.send_keys(char)
            time.sleep(delay)

    def wait_until_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable by {locator}'
        )

    def wait_until_clickable_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable by {locator}'
        ).click()

    def wait_until_visible(self, *locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element not visible by {locator}'
        )

    def wait_until_invisible(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element still visible by {locator}'
        )

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles # allways gives you a full list of open windows
        print('Current opened windows: ', all_windows)
        print('Switching to new window: ', all_windows[1])
        self.driver.switch_to.window(all_windows[1])

    def switch_to_window_by_id(self, window_id):
        print('Switching to new window: ', window_id)
        self.driver.switch_to.window(window_id)

    def hover_over_element(self, *locator):
        element = self.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, f'Expected text {expected_text} did not match actual {actual_text}'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f'Expected text {expected_text} not found in actual {actual_text}'

    def verify_url(self, expected_url):
        # current_url = self.driver.current_url
        # print(f'Current url {current_url}')
        # assert expected_url == current_url, f'Expected URL {expected_url}, but got {current_url}'
        self.wait.until(EC.url_to_be(expected_url), message=f'URL does not match {expected_url}')

    def verify_partial_url(self, expected_partial_url):
        # current_url = self.driver.current_url
        # print(f'Current url {current_url}')
        # assert expected_partial_url in current_url, f'Expected text {expected_partial_url} not in {current_url}'
        self.wait.until(EC.url_contains(expected_partial_url), message=f'URL does not contain {expected_partial_url}')

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def is_element_present(self, *locator):
        return len(self.driver.find_elements(*locator)) > 0
