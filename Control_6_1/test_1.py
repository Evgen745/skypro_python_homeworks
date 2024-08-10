from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from configuration import*
from time import sleep

def test_data_types_form(chrome_browser):
    chrome_browser.get(URL_1)
    
    # Данные для формы
    form_data = {
        "first-name": first_name,
        "last-name": last_name,
        "address": address,
        "e-mail": email,
        "phone": phone,
        "zip-code": zip_code,
        "city": city,
        "country": country,
        "job-position": job_position,
        "company": company
    }

    # Заполнение формы
    for field_name, value in form_data.items():
        chrome_browser.find_element(By.NAME, field_name).send_keys(value)

    # Нажатие на кнопку отправки
    WebDriverWait(chrome_browser, 40, 0.1).until(
        EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()
    sleep(2)

    # Ожидаемые классы для каждого поля
    field_classes = {
        "zip-code": "danger",
        "first-name": "success",
        "last-name": "success",
        "address": "success",  # Исправлено
        "e-mail": "success",
        "phone": "success",
        "city": "success",
        "country": "success",  # Исправлено
        "job-position": "success",
        "company": "success"
    }

    # Проверка классов полей
    for field_id, class_name in field_classes.items():
        field_element = chrome_browser.find_element(By.ID, field_id)
        assert class_name in field_element.get_attribute("class"), f"Field {field_id} does not have class {class_name}"