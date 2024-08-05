
import pytest
from selenium import webdriver
from pages.form_page import FormPage  

@pytest.fixture
def chrome_browser():
    driver = webdriver.Chrome()  
    yield driver
    driver.quit()  

def test_fill_form(chrome_browser):
    form_page = FormPage(chrome_browser)
    form_page.open()
    
    # Заполнение формы
    form_page.fill_form(
        "Иван", 
        "Петров", 
        "Ленина, 55-3", 
        "test@skypro.com", 
        "+7985899998787", 
        "", 
        "Москва", 
        "Россия", 
        "QA", 
        "SkyPro"
    )
    form_page.submit()

    # Проверка цвета полей
    assert form_page.get_zip_code_field_color() == 'rgb(255, 0, 0)'  # Красный цвет
    colors = form_page.get_other_fields_color()
    for color in colors.values():
        assert color == 'rgb(0, 128, 0)'  # Зеленый цвет