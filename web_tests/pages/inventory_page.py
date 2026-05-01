from selenium.webdriver.common.by import By
from web_tests.base.base_page import BasePage


class InventoryPage(BasePage):

    _ADD_TO_CART  = (By.CLASS_NAME, "btn_inventory")
    _CART_LINK    = (By.CLASS_NAME, "shopping_cart_link")
    _CART_CONTENT = (By.CLASS_NAME, "cart_list")  # confirma que o carrinho carregou

    def add_product(self) -> None:
        self.click(self._ADD_TO_CART)

    def go_to_cart(self) -> None:
        self.click(self._CART_LINK)
        self.wait_for_element(self._CART_CONTENT)  # espera elemento do carrinho