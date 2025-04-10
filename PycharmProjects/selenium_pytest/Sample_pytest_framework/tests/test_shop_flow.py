import sys
import os

from Sample_pytest_framework.pages.shop_page import ShopPage

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from selenium import webdriver

def test_complete_purchase():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/shop")

    shop_page = ShopPage(driver)
    shop_page.select_product("Blackberry")
    checkout_page = shop_page.go_to_checkout()
    checkout_page.complete_purchase("ind", "India")

    assert "Success!" in checkout_page.get_success_message()
    driver.quit()
