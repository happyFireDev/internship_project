import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from app.application import Application
from dotenv import load_dotenv

import os
from datetime import datetime

def before_all(context):
    # Load environment variables from .env file
    load_dotenv()

    # Access env variables

    # browserstack creds
    context.bs_user = os.getenv("BROWSERSTACK_USERNAME")
    context.bs_key = os.getenv("BROWSERSTACK_ACCESS_KEY")

    # https://soft.reelly.io/ qa automation creds
    context.user_email = os.getenv("REELLY_USER_EMAIL_ADDRESS")
    context.user_password = os.getenv("REELLY_USER_PASSWORD")

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    :param scenario_name: current test scenario name
    """
    # Change this as needed
    browser_name = 'chrome'  # or 'chrome', 'firefox', 'safari', 'browserstack'

    if browser_name == 'chrome':
        print("\nLaunching Local ChromeDriver")
        driver_path = ChromeDriverManager().install()
        service = Service(driver_path)
        options = ChromeOptions()
        # options.add_argument("--start-maximized")
        options.add_argument("--headless=new")  # headless
        options.add_argument("--window-size=1920,1080") # window size for headless
        context.driver = webdriver.Chrome(service=service, options=options)

    elif browser_name == 'firefox':
        print("\nLaunching Local FirefoxDriver")
        driver_path = GeckoDriverManager().install()
        service = FirefoxService(driver_path)
        options = FirefoxOptions()
        # options.add_argument("--start-maximized")
        options.add_argument("--headless") # headless
        options.add_argument("--window-size=1920,1080") # window size for headless
        context.driver = webdriver.Firefox(service=service, options=options)

    elif browser_name == 'safari':
        print("\nLaunching Local SafariDriver")
        context.driver = webdriver.Safari()

    elif browser_name == 'browserstack':
        print("\nLaunching BrowserStack Driver")

        url = f'https://{context.bs_user}:{context.bs_key}@hub-cloud.browserstack.com/wd/hub'

        if not context.bs_user or not context.bs_key:
            raise Exception("BrowserStack credentials are missing. Check your .env file.")

        bs_capabilities = [
            {
            "browserName": "Firefox",
            "browserVersion": "latest",
            "bstack:options": {
                "os": "Windows",
                "osVersion": "11",
                "sessionName": scenario_name,
                "buildName": "QA Automation Build"
            }
        },
        {
            "browserName": "Chrome",
            "browserVersion": "latest",
            "bstack:options": {
                "os": "OS X",
                "osVersion": "Monterey",
                "sessionName": scenario_name,
                "buildName": "QA Automation Build"
            }
        },
            {
                "browserName": "Safari",
                "browserVersion": "15.6",
                "bstack:options": {
                    "os": "OS X",
                    "osVersion": "Monterey",
                    "sessionName": scenario_name,
                    "buildName": "QA Automation Build"
                }
            }
        ]

        bs_capabilities = bs_capabilities[1]  # 👈 Pick one from the list

        options = ChromeOptions()
        options.set_capability('browserName', bs_capabilities["browserName"])
        options.set_capability('browserVersion', bs_capabilities["browserVersion"])
        options.set_capability('bstack:options', bs_capabilities["bstack:options"])

        context.driver = webdriver.Remote(command_executor=url, options=options)

    else:
        raise Exception(f"Browser '{browser_name}' is not supported")

    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)

#
# def after_step(context, step):
#     if step.status == 'failed':
#         print('\nStep failed: ', step)

#
# def after_step(context, step):
#     if step.status == 'failed':
#         print('\nStep failed: ', step)
#
#         # Create a screenshots directory if it doesn't exist
#         screenshots_dir = 'screenshots'
#         os.makedirs(screenshots_dir, exist_ok=True)
#
#         # Create a unique filename
#         timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#         screenshot_name = f"{screenshots_dir}/{step.name.replace(' ', '_')}_{timestamp}.png"
#
#         # Take screenshot
#         context.driver.save_screenshot(screenshot_name)
#         print(f"Screenshot saved: {screenshot_name}")

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)

        # Debug folder setup
        debug_dir = 'debug_dumps'
        os.makedirs(debug_dir, exist_ok=True)

        # Timestamp and filename base
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        base_name = step.name.replace(' ', '_')

        # Screenshot
        screenshot_path = f"{debug_dir}/{base_name}_{timestamp}.png"
        context.driver.save_screenshot(screenshot_path)
        print(f"🖼️ Screenshot saved: {screenshot_path}")

        # Current URL
        current_url = context.driver.current_url
        print(f"🌐 Current URL: {current_url}")

        # Cookies
        cookies = context.driver.get_cookies()
        print("🍪 Cookies:")
        for cookie in cookies:
            print(f"   {cookie['name']} = {cookie.get('value')}")

        # Optional: Dump page source (if you're stuck)
        html_path = f"{debug_dir}/{base_name}_{timestamp}.html"
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(context.driver.page_source)
        print(f"📄 Page source saved: {html_path}")


def after_scenario(context, scenario):
    print('\nScenario ended: ', scenario.name)
    context.driver.quit()
