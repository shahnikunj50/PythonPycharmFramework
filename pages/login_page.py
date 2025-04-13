from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username_input = (By.XPATH,"//input[@name = 'username']")
        self.password_input = (By.XPATH,"//input[@name = 'password']")
        self.login_button = (By.XPATH,"//button[@type= 'submit']")

    #Actions
    def load(self, url):
        self.driver.get(url)

    def enter_username(self,username):
        self.driver.find_element(*self.username_input).send_keys("username")

    def enter_password(self,password):
        self.driver.find_element(*self.password_input).send_keys("password")

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self,username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
