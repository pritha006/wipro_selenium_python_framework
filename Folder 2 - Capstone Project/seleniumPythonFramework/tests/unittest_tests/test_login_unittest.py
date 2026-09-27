from pathlib import Path
import unittest

from pages.home_page import HomePage
from pages.login_page import LoginPage

from utils.driver_factory import DriverFactory
from utils.config_reader import ConfigReader
from utils.csv_reader import CSVReader
from utils.screenshot import Screenshot


class TestLoginUnittest(
    unittest.TestCase
):

    @classmethod
    def setUpClass(cls):

        base_dir = (
            Path(__file__)
            .resolve()
            .parents[2]
        )

        csv_path = (
            base_dir
            / "test_data"
            / "login_data.csv"
        )

        cls.login_data = (
            CSVReader.read_csv(
                csv_path
            )
        )

    def setUp(self):

        self.driver = (
            DriverFactory.get_driver()
        )

        self.home_page = (
            HomePage(
                self.driver
            )
        )

        self.login_page = (
            LoginPage(
                self.driver
            )
        )

    def test_login_data(self):

        for user in self.login_data:

            with self.subTest(
                email=user["email"]
            ):

                self.home_page.open(
                    ConfigReader
                    .get_base_url()
                )

                self.home_page.go_to_login_page()

                self.login_page.login(
                    user["email"],
                    user["password"]
                )

                try:

                    if (
                        user[
                            "expected_result"
                        ]
                        == "success"
                    ):

                        self.assertTrue(
                            self.login_page
                            .is_login_successful()
                        )

                    elif (
                        user[
                            "expected_result"
                        ]
                        == "failure"
                    ):

                        self.assertNotEqual(
                            self.login_page
                            .get_warning_message(),
                            ""
                        )

                except AssertionError:

                    Screenshot.capture(
                        self.driver,
                        "unittest_login_failure"
                    )

                    raise

    def test_valid_login(self):

        email, password = ConfigReader.get_valid_credentials()
        if not email or not password:
            self.skipTest(
                "Set valid_email and valid_password in config/config.ini to run this test"
            )

        try:
            self.home_page.open(ConfigReader.get_base_url())
            self.home_page.go_to_login_page()
            self.login_page.login(email, password)
            self.assertTrue(self.login_page.is_login_successful())
        except Exception:
            Screenshot.capture(self.driver, "unittest_valid_login_failure")
            raise

    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":

    unittest.main()
