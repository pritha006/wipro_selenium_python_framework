import pytest

from utils.driver_factory import DriverFactory
from utils.screenshot import Screenshot


def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        default=None,
        help="Browser to use (currently: chrome)",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=None,
        help="Run Chrome without a visible window",
    )


@pytest.fixture
def driver(request):

    driver = (
        DriverFactory.get_driver(
            browser=request.config.getoption("browser"),
            headless=request.config.getoption("headless"),
        )
    )

    yield driver

    driver.quit()


@pytest.hookimpl(
    hookwrapper=True
)
def pytest_runtest_makereport(
    item,
    call
):

    outcome = yield

    report = outcome.get_result()

    if (
        report.when == "call"
        and report.failed
    ):

        driver = item.funcargs.get(
            "driver"
        )

        if driver:

            Screenshot.capture(
                driver,
                item.name
            )
