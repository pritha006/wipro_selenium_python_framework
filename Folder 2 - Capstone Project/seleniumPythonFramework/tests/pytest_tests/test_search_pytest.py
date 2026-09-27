from pathlib import Path

import pytest

from pages.home_page import HomePage
from pages.search_page import SearchPage

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
    / "search_data.csv"
)

SEARCH_DATA = (
    CSVReader.read_csv(
        CSV_PATH
    )
)


@pytest.mark.parametrize(
    "data",
    SEARCH_DATA
)
def test_product_search(
    driver,
    data
):

    home_page = HomePage(
        driver
    )

    search_page = SearchPage(
        driver
    )

    home_page.open(
        ConfigReader.get_base_url()
    )

    home_page.search_product(
        data["product"]
    )

    has_results = (
        search_page
        .has_search_results()
    )

    if (
        data["expected_result"]
        == "success"
    ):

        assert has_results, (
            f"No results found for "
            f"{data['product']}"
        )

    elif (
        data["expected_result"]
        == "failure"
    ):

        assert not has_results, (
            f"Unexpected results found "
            f"for {data['product']}"
        )

    else:

        pytest.fail(
            "Invalid expected_result "
            "value in CSV"
        )