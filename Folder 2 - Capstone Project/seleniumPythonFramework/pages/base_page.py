from utils.waits import Waits


class BasePage:

    def __init__(self, driver):

        self.driver = driver
        self.waits = Waits(driver)

    def click(self, locator):

        self.waits.clickable(
            locator
        ).click()

    def enter_text(
        self,
        locator,
        text
    ):

        element = self.waits.visible(
            locator
        )

        element.clear()

        element.send_keys(
            text
        )

    def get_text(self, locator):

        return self.waits.visible(
            locator
        ).text

    def get_texts(self, locator):

        return [
            element.text.strip()
            for element in self.waits.all_visible(locator)
            if element.text.strip()
        ]

    def is_visible(
        self,
        locator
    ):

        try:

            self.waits.visible(
                locator
            )

            return True

        except Exception:

            return False
