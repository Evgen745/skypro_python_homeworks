import pytest
from selenium import webdriver
from pages.calculator_page import CalculatorPage

@pytest.fixture
def chrome_browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calculator_form(chrome_browser):
    calc_page = CalculatorPage(chrome_browser)
    calc_page.open()

    # Заполняем поле задержки
    calc_page.enter_delay(1)

    # Кликаем на кнопки калькулятора
    calc_page.click_calculator_buttons()

    # Получаем текст результата
    result_text = calc_page.get_result()

    # Проверяем, что результат равен 15
    assert result_text == "15", f"Expected result to be '15', but got '{result_text}'"