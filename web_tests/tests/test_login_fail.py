from selenium.webdriver.common.by import By
from web_tests.base.base_test import BaseTest
from web_tests.pages.login_page import LoginPage

class TestLoginFail(BaseTest):

    def test_invalid_login(self):
        login = LoginPage(self.driver)

        login.login("usuario_errado", "senha_errada")

        error = self.driver.find_element(By.CLASS_NAME, "error-message-container").text

        assert "Epic sadface" in error