from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class SearchPage(BasePage):

    PRODUCT_NAMES = (
        By.CSS_SELECTOR,
        ".product-thumb h4 a"
    )

    NO_RESULTS_MESSAGE = (
        By.XPATH,
        "//*[contains(text(), 'There is no product')]"
    )

    def get_product_names(self):
        self.wait_for_search_to_finish()
        return [
            element.text.strip()
            for element in self.driver.find_elements(*self.PRODUCT_NAMES)
            if element.text.strip()
        ]

    def wait_for_search_to_finish(self):

        WebDriverWait(self.driver, 10).until(
            lambda driver: (
                driver.find_elements(*self.PRODUCT_NAMES)
                or driver.find_elements(*self.NO_RESULTS_MESSAGE)
            )
        )

    def has_search_results(self):

        return (
            len(
                self.get_product_names()
            ) > 0
        )

    def has_no_results_message(self):
        self.wait_for_search_to_finish()
        return self.is_visible(
            self.NO_RESULTS_MESSAGE
        )
