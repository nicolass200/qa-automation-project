from selenium.webdriver.common.by import By
from web_tests.base.base_page import BasePage


class CheckoutPage(BasePage):

    _FIRST_NAME  = (By.ID, "first-name")
    _LAST_NAME   = (By.ID, "last-name")
    _POSTAL_CODE = (By.ID, "postal-code")
    _CONTINUE    = (By.ID, "continue")
    _FINISH      = (By.ID, "finish")
    _COMPLETE    = (By.CLASS_NAME, "complete-header")  # confirma compra finalizada

    def fill_data(self, first: str = "Nicolas", last: str = "Test", postal: str = "12345") -> None:
        self.type_text(self._FIRST_NAME, first)
        self.type_text(self._LAST_NAME, last)
        self.type_text(self._POSTAL_CODE, postal)
        self.click(self._CONTINUE)
        self.wait_for_element(self._FINISH)  # espera botão finish aparecer

    def finish(self) -> None:
        finish_btn = self.find(self._FINISH)
        self.scroll_to(finish_btn)
        self.click(self._FINISH)
        self.wait_for_element(self._COMPLETE)  # espera tela de confirmação