import pytest
import allure
from selenium import webdriver
from selenium.webdriver.safari.options import Options as SafariOptions
from typing import Generator, Any
from _pytest.fixtures import FixtureRequest


def pytest_addoption(parser: Any) -> None:
    parser.addoption(
        "--browser",
        action="store",
        default="safari",
        help="Browser to run tests: safari"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless mode (not for Safari)"
    )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        try:
            if "driver" in item.funcargs:
                driver = item.funcargs["driver"]
                take_screenshot(driver, item.name)
                attach_page_source(driver, item.name)
        except Exception as e:
            print(f"Failed to attach debug information to Allure: {e}")


def take_screenshot(driver: webdriver.Remote, test_name: str) -> None:
    try:
        screenshot = driver.get_screenshot_as_png()
        allure.attach(
            screenshot,
            name=f"screenshot_{test_name}",
            attachment_type=allure.attachment_type.PNG
        )
    except Exception as e:
        print(f"Failed to take screenshot: {e}")


def attach_page_source(driver: webdriver.Remote, test_name: str) -> None:
    try:
        page_source = driver.page_source
        allure.attach(
            page_source,
            name=f"page_source_{test_name}",
            attachment_type=allure.attachment_type.HTML
        )
    except Exception as e:
        print(f"Failed to attach page source: {e}")


@pytest.fixture(scope="function")
def driver(request: FixtureRequest) -> Generator[webdriver.Remote, None, None]:
    browser_name = request.config.getoption("--browser")

    with allure.step(f"Initialize {browser_name} driver"):
        if browser_name == "safari":
            options = SafariOptions()
            driver_instance = webdriver.Safari(options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        driver_instance.maximize_window()
        driver_instance.implicitly_wait(10)

    yield driver_instance

    with allure.step("Close browser"):
        driver_instance.quit()


@pytest.fixture
def login_page(driver: webdriver.Remote) -> Any:
    from pages.login_page import LoginPage
    return LoginPage(driver)


@pytest.fixture
def products_page(driver: webdriver.Remote) -> Any:
    from pages.products_page import ProductsPage
    return ProductsPage(driver)