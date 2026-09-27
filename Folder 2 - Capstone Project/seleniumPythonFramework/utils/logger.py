import logging
from pathlib import Path


class Logger:

    @staticmethod
    def get_logger(name):

        logger = logging.getLogger(name)

        logger.setLevel(logging.INFO)

        if not logger.handlers:

            base_dir = (
                Path(__file__)
                .resolve()
                .parent
                .parent
            )

            log_dir = (
                base_dir / "logs"
            )

            log_dir.mkdir(
                exist_ok=True
            )

            log_file = (
                log_dir / "automation.log"
            )

            handler = logging.FileHandler(
                log_file,
                encoding="utf-8"
            )

            formatter = logging.Formatter(
                "%(asctime)s | "
                "%(levelname)s | "
                "%(name)s | "
                "%(message)s"
            )

            handler.setFormatter(
                formatter
            )

            logger.addHandler(
                handler
            )

        return logger