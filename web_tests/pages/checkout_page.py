from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    def fill_data(self):
        self.driver.find_element(By.ID, "first-name").send_keys("Nicolas")
        self.driver.find_element(By.ID, "last-name").send_keys("Test")
        self.driver.find_element(By.ID, "postal-code").send_keys("12345")
        self.driver.find_element(By.ID, "continue").click()

    def finish(self):
        wait = WebDriverWait(self.driver, 20)

        wait.until(EC.url_contains("checkout-step-two"))

        finish_button = wait.until(
            EC.presence_of_element_located((By.ID, "finish"))
        )

        self.driver.execute_script("arguments[0].scrollIntoView(true);", finish_button)

        wait.until(EC.element_to_be_clickable((By.ID, "finish")))

        finish_button.click()