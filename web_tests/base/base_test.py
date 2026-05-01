from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import Config


class BaseTest:

    def setup_method(self) -> None:
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=self._build_options(),
        )
        self.driver.get(Config.WEB_BASE_URL)

    def teardown_method(self) -> None:
        if self.driver:
            self.driver.quit()

    @staticmethod
    def _build_options() -> Options:
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")  # evita elementos fora da viewport
        return options