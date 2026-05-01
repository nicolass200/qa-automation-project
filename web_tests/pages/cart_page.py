from selenium.webdriver.common.by import By
from web_tests.base.base_page import BasePage


class CartPage(BasePage):

    _CHECKOUT_BUTTON = (By.ID, "checkout")
    _FIRST_NAME      = (By.ID, "first-name")  # confirma checkout step-one carregou

    def checkout(self) -> None:
        self.click(self._CHECKOUT_BUTTON)
        self.wait_for_element(self._FIRST_NAME)  # espera formulário de checkout