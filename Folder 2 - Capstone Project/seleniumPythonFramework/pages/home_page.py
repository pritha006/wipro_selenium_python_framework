from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):

    MY_ACCOUNT = (
        By.CSS_SELECTOR,
        "a[title='My Account']"
    )

    LOGIN = (
        By.LINK_TEXT,
        "Login"
    )

    SEARCH_BOX = (
        By.NAME,
        "search"
    )

    SEARCH_BUTTON = (
        By.CSS_SELECTOR,
        "#search button"
    )

    def open(self, url):

        self.driver.get(url)
        self.waits.visible(self.SEARCH_BOX)

    def go_to_login_page(self):

        self.click(
            self.MY_ACCOUNT
        )

        self.click(
            self.LOGIN
        )

    def search_product(
        self,
        product
    ):

        self.enter_text(
            self.SEARCH_BOX,
            product
        )

        self.click(
            self.SEARCH_BUTTON
        )
