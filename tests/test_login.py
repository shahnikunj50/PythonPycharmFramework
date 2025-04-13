import config
from pages.login_page import LoginPage

def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.load(config.BASE_URL)
    login_page.login(config.USERNAME, config.PASSWORD)

    # Simple assertion to check if login was successful
    assert "dashboard" in driver.current_url.lower() or "index" in driver.current_url.lower()