import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from utils.attach import Attach
from selene import Browser, Config


@pytest.fixture(scope='session')
def browser_chrome():
    capabilities = DesiredCapabilities.CHROME

    capabilities.update({
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
        },
        "goog:loggingPrefs": {
            "browser": "ALL"
        }

    })
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        desired_capabilities=capabilities
    )
    driver.set_window_size(1920, 1080)

    browser = Browser(Config(driver=driver))
    yield browser
    Attach().add_png(browser)
    Attach().add_video(browser)
    Attach().add_logs(browser)
    Attach().add_html(browser)
    browser.quit()
