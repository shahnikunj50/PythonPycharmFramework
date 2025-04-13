import config
from pages.login_page import LoginPage
import time

def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.load(config.BASE_URL)
    login_page.login(config.USERNAME,config.PASSWORD)
    assert "index" in driver.current_url.lower()
