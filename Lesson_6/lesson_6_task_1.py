from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

def test_ajax_request(browser):
    # Инициализация драйвера
    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError("Поддерживаются только 'firefox' и 'chrome'")

    wait = WebDriverWait(driver, 40, 0.1)

    try:
        driver.get("http://uitestingplayground.com/ajax")

        # Находим кнопку и кликаем по ней
        blue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ajaxButton")))
        blue_button.click()  # Вызываем метод click

        # Ожидаем появления элемента с текстом
        text_from_content = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".bg-success"))).text
        
        sleep(2)  # Ждем 2 секунды для визуализации
        print(text_from_content)  # Выводим текст

    except Exception as ex:
        print(ex)
    finally:
        driver.quit()

# Запуск теста для Firefox
test_ajax_request("firefox")

# Запуск теста для Chrome
test_ajax_request("chrome")
