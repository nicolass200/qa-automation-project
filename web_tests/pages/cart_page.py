from selenium.webdriver.common.by import By
from web_tests.base.base_page import BasePage


class CartPage(BasePage):

    _FIRST_NAME = (By.ID, "first-name")

    def checkout(self) -> None:
        self.navigate_to("checkout-step-one.html")
        self.wait_for_element(self._FIRST_NAME)