from selenium.webdriver.common.by import By
from web_tests.base.base_page import BasePage


class LoginPage(BasePage):

    _USERNAME      = (By.ID, "user-name")
    _PASSWORD      = (By.ID, "password")
    _LOGIN_BUTTON  = (By.ID, "login-button")
    _INVENTORY     = (By.ID, "inventory_container")

    def invalid_login(self, user, password):
        self.driver.find_element(By.ID, "user-name").send_keys(user)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def login(self, username: str, password: str) -> None:
        self.type_text(self._USERNAME, username)
        self.type_text(self._PASSWORD, password)
        self.click(self._LOGIN_BUTTON)
        self.wait_for_element(self._INVENTORY) 
        
        