from selenium.webdriver.common.by import By
from web_tests.base.base_page import BasePage


class CartPage(BasePage):

    _CHECKOUT_BUTTON = (By.ID, "checkout")

    def checkout(self) -> None:
        self.click(self._CHECKOUT_BUTTON)
        self.wait_for_url("checkout-step-one")