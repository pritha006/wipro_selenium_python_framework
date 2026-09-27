from pathlib import Path

import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage

from utils.config_reader import ConfigReader
from utils.csv_reader import CSVReader


BASE_DIR = (
    Path(__file__)
    .resolve()
    .parents[2]
)

CSV_PATH = (
    BASE_DIR
    / "test_data"
    / "login_data.csv"
)

LOGIN_DATA = (
    CSVReader.read_csv(
        CSV_PATH
    )
)


@pytest.mark.parametrize(
    "user",
    LOGIN_DATA
)
def test_login(
    driver,
    user
):

    home_page = HomePage(
        driver
    )

    login_page = LoginPage(
        driver
    )

    home_page.open(
        ConfigReader.get_base_url()
    )

    home_page.go_to_login_page()

    login_page.login(
        user["email"],
        user["password"]
    )

    if (
        user["expected_result"]
        == "success"
    ):

        assert (
            login_page
            .is_login_successful()
        ), (
            f"Login failed for "
            f"{user['email']}"
        )

    elif (
        user["expected_result"]
        == "failure"
    ):

        assert (
            login_page
            .get_warning_message()
            != ""
        ), (
            "Expected warning "
            "message not displayed"
        )

    else:

        pytest.fail(
            "Invalid expected_result "
            "value in CSV"
        )


def test_valid_login(driver):
    """Runs only after valid_email and valid_password are configured locally."""
    email, password = ConfigReader.get_valid_credentials()
    if not email or not password:
        pytest.skip("Set valid_email and valid_password in config/config.ini to run this test")

    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    home_page.open(ConfigReader.get_base_url())
    home_page.go_to_login_page()
    login_page.login(email, password)

    assert login_page.is_login_successful(), f"Login failed for {email}"
