from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config_reader import ConfigReader


class Waits:

    def __init__(self, driver):

        self.wait = WebDriverWait(
            driver,
            ConfigReader.get_timeout()
        )

    def visible(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def clickable(self, locator):

        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def present(self, locator):

        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def all_visible(self, locator):

        return self.wait.until(
            EC.visibility_of_all_elements_located(locator)
        )

    def url_contains(self, value):

        return self.wait.until(
            EC.url_contains(value)
        )
