from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    def fill_data(self):
        wait = WebDriverWait(self.driver, 15)

        wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Nicolas")
        self.driver.find_element(By.ID, "last-name").send_keys("Test")
        self.driver.find_element(By.ID, "postal-code").send_keys("12345")

        self.driver.find_element(By.ID, "continue").click()

    def finish(self):
        wait = WebDriverWait(self.driver, 20)

        # Espera o botão FINISH existir (em vez de URL)
        finish_button = wait.until(
            EC.presence_of_element_located((By.ID, "finish"))
        )

        # Scroll (CI precisa disso)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", finish_button)

        # Espera clicável
        wait.until(EC.element_to_be_clickable((By.ID, "finish")))

        finish_button.click()