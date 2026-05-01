from selenium.webdriver.common.by import By
from web_tests.base.base_test import BaseTest
from web_tests.pages.login_page import LoginPage
from web_tests.pages.inventory_page import InventoryPage
from web_tests.pages.cart_page import CartPage
from web_tests.pages.checkout_page import CheckoutPage
from config import Config


class TestE2E(BaseTest):

    def test_complete_purchase(self) -> None:
        LoginPage(self.driver).login(Config.VALID_USER, Config.VALID_PASSWORD)
        
        inventory = InventoryPage(self.driver)
        inventory.add_product()
        inventory.go_to_cart()

        CartPage(self.driver).checkout()

        checkout = CheckoutPage(self.driver)
        checkout.fill_data()
        checkout.finish()

        success_text = self.driver.find_element(By.CLASS_NAME, "complete-header").text
        assert "THANK YOU" in success_text.upper(), (
            f"Compra não finalizada. Texto encontrado: '{success_text}'"
        )