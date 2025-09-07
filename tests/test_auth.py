import pytest
import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


class TestAuthentication:

    @pytest.mark.parametrize("username,password", [
        ("standard_user", "secret_sauce"),
    ])
    def test_successful_login(
            self,
            driver: WebDriver,
            login_page: LoginPage,
            products_page: ProductsPage,
            username: str,
            password: str
    ) -> None:
        with allure.step("Open login page"):
            login_page.open()
            assert login_page.is_opened(), "Login page should be opened"

        with allure.step("Enter credentials and login"):
            login_page.login(username, password)

        with allure.step("Verify products page is opened"):
            assert products_page.is_opened(), "Products page should be opened after successful login"

            products_count = products_page.get_products_count()
            assert products_count > 0, f"Should display products, found {products_count}"

            page_title = products_page.get_page_title()
            assert page_title == "Products", f"Page title should be 'Products', got '{page_title}'"

    def test_logout(
            self,
            driver: WebDriver,
            login_page: LoginPage,
            products_page: ProductsPage
    ) -> None:
        with allure.step("Login to application"):
            login_page.open()
            assert login_page.is_opened(), "Login page should be opened"
            login_page.login("standard_user", "secret_sauce")
            assert products_page.is_opened(), "Should be logged in"

        with allure.step("Perform logout"):
            products_page.logout()

        with allure.step("Verify logout successful"):
            assert login_page.is_opened(), "Should be redirected to login page after logout"