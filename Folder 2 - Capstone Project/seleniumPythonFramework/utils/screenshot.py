from datetime import datetime
from pathlib import Path


class Screenshot:

    @staticmethod
    def capture(driver, test_name):

        base_dir = Path(__file__).resolve().parent.parent

        screenshot_dir = (
            base_dir / "screenshots"
        )

        screenshot_dir.mkdir(
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        file_name = (
            f"{test_name}_{timestamp}.png"
        )

        file_path = (
            screenshot_dir / file_name
        )

        driver.save_screenshot(
            str(file_path)
        )

        return file_path