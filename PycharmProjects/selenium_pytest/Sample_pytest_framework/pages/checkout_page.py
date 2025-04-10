from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def complete_purchase(self, partial_country, full_country):
        self.driver.find_element(By.ID, "country").send_keys(partial_country)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, full_country)))
        self.driver.find_element(By.LINK_TEXT, full_country).click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

    def get_success_message(self):
        return self.driver.find_element(By.CLASS_NAME, "alert-success").text
