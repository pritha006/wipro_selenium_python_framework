# Selenium Python Automation Framework

## Objective

This capstone project automates the **Login** and **Product Search** journeys on
[TutorialsNinja demo store](https://tutorialsninja.com/demo/). It demonstrates a
scalable Selenium framework using both **PyTest** and **unittest**, Page Object
Model (POM), INI-based configuration, CSV test data, failure screenshots and a
PyTest HTML report.

## Project structure

```text
config/       Browser, URL, timeout and optional valid-login settings
pages/        POM classes: HomePage, LoginPage and SearchPage
test_data/    CSV-driven negative-login and search scenarios
tests/        Equivalent PyTest and unittest suites
utils/        Driver, wait, configuration, CSV, logging and screenshot helpers
reports/      Generated PyTest HTML report
screenshots/  Captures created for failed tests
```

## Setup

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Chrome must be installed. Selenium Manager obtains the matching ChromeDriver.

## Run the tests

```powershell
# PyTest suite, with HTML report at reports/report.html
pytest --headless

# unittest suite
python -m unittest discover -s tests/unittest_tests -p "test_*.py"
```

The CSV login cases intentionally use invalid credentials and verify the warning
message. To exercise a successful login, register a TutorialsNinja demo account,
then set `valid_email` and `valid_password` in `config/config.ini` (do not commit
them) or use `SELENIUM_VALID_EMAIL` and `SELENIUM_VALID_PASSWORD` environment
variables. The positive test is skipped until both values are present, so the
framework remains runnable without committing credentials. Set
`SELENIUM_HEADLESS=true` for headless unittest execution.

## Design notes

- Page classes keep locators and browser actions out of tests.
- Explicit waits replace fixed `sleep` calls for reliable synchronization.
- CSV files drive product-search and negative-login inputs.
- PyTest captures a screenshot through its failure hook; unittest captures one
  when an assertion fails.
