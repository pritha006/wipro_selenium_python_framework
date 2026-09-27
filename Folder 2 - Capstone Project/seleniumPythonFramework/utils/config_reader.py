import configparser
import os
from pathlib import Path


class ConfigReader:

    BASE_DIR = Path(__file__).resolve().parent.parent

    CONFIG_PATH = (
        BASE_DIR
        / "config"
        / "config.ini"
    )

    @classmethod
    def get_config(cls):

        config = configparser.ConfigParser()

        config.read(cls.CONFIG_PATH)

        return config["DEFAULT"]

    @classmethod
    def get_base_url(cls):

        return cls.get_config().get(
            "base_url"
        )

    @classmethod
    def get_browser(cls):

        return cls.get_config().get(
            "browser",
            "chrome"
        )

    @classmethod
    def get_timeout(cls):

        return cls.get_config().getint(
            "timeout",
            10
        )

    @classmethod
    def get_headless(cls):

        value = os.getenv("SELENIUM_HEADLESS")
        if value is not None:
            return value.strip().lower() in {"1", "true", "yes"}

        return cls.get_config().getboolean("headless", False)

    @classmethod
    def get_valid_credentials(cls):

        config = cls.get_config()
        return (
            os.getenv("SELENIUM_VALID_EMAIL", config.get("valid_email", "")).strip(),
            os.getenv("SELENIUM_VALID_PASSWORD", config.get("valid_password", "")).strip(),
        )
