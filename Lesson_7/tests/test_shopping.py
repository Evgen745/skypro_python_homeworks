import pytest
from selenium import webdriver
from pages.shopping_page import ShoppingPage

@pytest.fixture
def chrome_browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_shopping(chrome_browser):
    shopping_page = ShoppingPage(chrome_browser)
    shopping_page.open()
    shopping_page.login("standard_user", "secret_sauce")
    shopping_page.add_to_cart()
    shopping_page.checkout("Имя", "Фамилия", "12345")

    total = shopping_page.get_total()
    assert total == "$58.29"