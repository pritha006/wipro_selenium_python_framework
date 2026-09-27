from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL = (
        By.ID,
        "input-email"
    )

    PASSWORD = (
        By.ID,
        "input-password"
    )

    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        "input[value='Login']"
    )

    ACCOUNT_HEADING = (
        By.XPATH,
        "//h2[normalize-space()='My Account']"
    )

    WARNING_MESSAGE = (
        By.CSS_SELECTOR,
        ".alert-danger"
    )

    def login(
        self,
        email,
        password
    ):

        self.enter_text(
            self.EMAIL,
            email
        )

        self.enter_text(
            self.PASSWORD,
            password
        )

        self.click(
            self.LOGIN_BUTTON
        )

    def is_login_successful(self):

        return (
            "account/account" in self.driver.current_url
            and self.is_visible(self.ACCOUNT_HEADING)
        )

    def get_warning_message(self):

        if self.is_visible(
            self.WARNING_MESSAGE
        ):

            return self.get_text(
                self.WARNING_MESSAGE
            )

        return ""
