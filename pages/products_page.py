from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Any, List


class ProductsPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def is_opened(self) -> bool:
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
            )
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
            )
            return True
        except:
            return False

    def get_products_count(self) -> int:
        try:
            products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
            return len(products)
        except:
            return 0

    def get_page_title(self) -> str:
        try:
            title_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "title"))
            )
            return title_element.text
        except:
            return ""

    def open_menu(self) -> None:
        try:
            menu_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
            )
            menu_button.click()
        except:
            pass

    def logout(self) -> None:
        self.open_menu()
        try:
            logout_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
            )
            logout_link.click()
        except:
            pass

    def is_logged_out(self) -> bool:
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("saucedemo.com")
            )
            return self.driver.current_url == "https://www.saucedemo.com/"
        except:
            return False