from pathlib import Path
import unittest

from pages.home_page import HomePage
from pages.search_page import SearchPage

from utils.driver_factory import DriverFactory
from utils.config_reader import ConfigReader
from utils.csv_reader import CSVReader
from utils.screenshot import Screenshot


class TestSearchUnittest(
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
            / "search_data.csv"
        )

        cls.search_data = (
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

        self.search_page = (
            SearchPage(
                self.driver
            )
        )

    def test_product_search_data(self):

        for data in self.search_data:

            with self.subTest(
                product=data["product"]
            ):

                self.home_page.open(
                    ConfigReader
                    .get_base_url()
                )

                self.home_page.search_product(
                    data["product"]
                )

                try:

                    has_results = (
                        self.search_page
                        .has_search_results()
                    )

                    if (
                        data[
                            "expected_result"
                        ]
                        == "success"
                    ):

                        self.assertTrue(
                            has_results
                        )

                    elif (
                        data[
                            "expected_result"
                        ]
                        == "failure"
                    ):

                        self.assertFalse(
                            has_results
                        )

                except AssertionError:

                    Screenshot.capture(
                        self.driver,
                        "unittest_search_failure"
                    )

                    raise

    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":

    unittest.main()