from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.config_reader import ConfigReader


class DriverFactory:

    @staticmethod
    def get_driver(browser=None, headless=None):

        browser = (browser or ConfigReader.get_browser()).lower()

        if browser == "chrome":

            options = Options()

            if headless if headless is not None else ConfigReader.get_headless():
                options.add_argument("--headless=new")

            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")

            driver = webdriver.Chrome(
                options=options
            )

        else:

            raise ValueError(
                f"Unsupported browser: {browser}"
            )

        driver.set_page_load_timeout(30)
        driver.implicitly_wait(0)

        return driver
