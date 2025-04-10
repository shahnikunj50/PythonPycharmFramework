from selenium.webdriver.common.by import By

from Sample_pytest_framework.pages.checkout_page import CheckoutPage


class ShopPage:
    def __init__(self, driver):
        self.driver = driver

    def select_product(self, product_name):
        allitems = self.driver.find_elements(By.XPATH,"//div[@class='card h-100']")
        for label in allitems:
            pname = label.find_element(By.XPATH,"div/h4/a").text
            if pname == product_name:
                label.find_element(By.XPATH,"div/button").click()

    def go_to_checkout(self):
        self.driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
        return CheckoutPage(self.driver)
