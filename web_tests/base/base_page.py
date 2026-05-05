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
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.scroll_to(element)
        try:
            element.click()
        except Exception:
            # JS click como fallback — funciona mesmo quando o clique nativo falha no headless
            self.driver.execute_script("arguments[0].click();", element)

    def type_text(self, locator: tuple, text: str) -> None:
        self.find(locator).send_keys(text)

    def navigate_to(self, path: str) -> None:
        """Navegação direta por URL — mais confiável que clicar em links no CI."""
        self.driver.get(f"{Config.WEB_BASE_URL}{path}")

    def scroll_to(self, element: WebElement) -> None:
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def wait_for_element(self, locator: tuple) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))