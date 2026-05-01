from web_tests.base.base_test import BaseTest
from web_tests.pages.login_page import LoginPage
from web_tests.pages.inventory_page import InventoryPage
from web_tests.pages.cart_page import CartPage
from web_tests.pages.checkout_page import CheckoutPage

class TestE2E(BaseTest):

    def test_complete_purchase(self):
        login = LoginPage(self.driver)
        login.login("standard_user", "secret_sauce")

        inventory = InventoryPage(self.driver)
        inventory.add_product()
        inventory.go_to_cart()

        cart = CartPage(self.driver)
        cart.checkout()

        checkout = CheckoutPage(self.driver)
        checkout.fill_data()
        checkout.finish()

        assert "checkout-complete" in self.driver.current_url