from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from config import Config


class BasePage:

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.WAIT_TIMEOUT)

    def find(self, locator: tuple) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator: tuple) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator: tuple, text: str) -> None:
        self.find(locator).send_keys(text)

    def scroll_to(self, element: WebElement) -> None:
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def wait_for_element(self, locator: tuple) -> WebElement:
        """Aguarda um elemento que confirme visualmente que a página carregou."""
        return self.wait.until(EC.visibility_of_element_located(locator))