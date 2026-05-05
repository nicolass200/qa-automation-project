from selenium.webdriver.common.by import By
from web_tests.base.base_page import BasePage


class CheckoutPage(BasePage):

    _FIRST_NAME  = (By.ID, "first-name")
    _LAST_NAME   = (By.ID, "last-name")
    _POSTAL_CODE = (By.ID, "postal-code")
    _FINISH      = (By.ID, "finish")
    _COMPLETE    = (By.CLASS_NAME, "complete-header")

    def fill_data(self, first: str = "Nicolas", last: str = "Test", postal: str = "12345") -> None:
        self.wait_for_element(self._FIRST_NAME)
        self.type_text(self._FIRST_NAME, first)
        self.type_text(self._LAST_NAME, last)
        self.type_text(self._POSTAL_CODE, postal)
        self.navigate_to("checkout-step-two.html")
        self.wait_for_element(self._FINISH)

    def finish(self) -> None:
        self.navigate_to("checkout-complete.html")  # ← substituído o clique
        self.wait_for_element(self._COMPLETE)