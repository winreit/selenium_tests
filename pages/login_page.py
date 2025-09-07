from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Any


class LoginPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def open(self) -> None:
        self.driver.get(self.url)

    def is_opened(self) -> bool:
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "user-name"))
            )
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "password"))
            )
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "login-button"))
            )
            return True
        except:
            return False

    def login(self, username: str, password: str) -> None:
        username_field = self.driver.find_element(By.ID, "user-name")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        username_field.clear()
        username_field.send_keys(username)

        password_field.clear()
        password_field.send_keys(password)

        login_button.click()

    def get_error_message(self) -> str:
        try:
            error_element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
            )
            return error_element.text
        except:
            return ""