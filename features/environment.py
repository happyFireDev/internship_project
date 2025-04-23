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

# Load environment variables
load_dotenv()


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    :param scenario_name: current test scenario name
    """
    # Change this as needed
    browser_name = 'chrome'  # or 'firefox', 'safari', 'browserstack'

    if browser_name == 'chrome':
        print("\nLaunching Local ChromeDriver")
        driver_path = ChromeDriverManager().install()
        service = Service(driver_path)
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        context.driver = webdriver.Chrome(service=service, options=options)

    elif browser_name == 'firefox':
        print("\nLaunching Local FirefoxDriver")
        driver_path = GeckoDriverManager().install()
        service = FirefoxService(driver_path)
        options = FirefoxOptions()
        options.add_argument("--start-maximized")
        context.driver = webdriver.Firefox(service=service, options=options)

    elif browser_name == 'safari':
        print("\nLaunching Local SafariDriver")
        context.driver = webdriver.Safari()

    elif browser_name == 'browserstack':
        print("\nLaunching BrowserStack Driver")
        bs_user = os.getenv('BROWSERSTACK_USERNAME')
        bs_key = os.getenv('BROWSERSTACK_ACCESS_KEY')
        url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

        bs_capabilities = {
            "browserName": "Chrome",
            "browserVersion": "latest",
            "bstack:options": {
                "os": "Windows",
                "osVersion": "11",
                "sessionName": scenario_name,
                "buildName": "QA Automation Build"
            }
        }

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


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, scenario):
    print('\nScenario ended: ', scenario.name)
    context.driver.quit()
