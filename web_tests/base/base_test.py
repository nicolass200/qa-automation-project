from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BaseTest:

    def setup_method(self):
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.driver.get("https://www.saucedemo.com/")

    def teardown_method(self):
        self.driver.quit()