from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

def test_input_field(browser):
    # Инициализация драйвера
    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError("Поддерживаются только 'firefox' и 'chrome'")

    try:
        driver.get("https://the-internet.herokuapp.com/inputs")
        
        # Находим поле ввода
        input_field = driver.find_element(By.TAG_NAME, "input")
        
        # Вводим значение "1000"
        input_field.send_keys("1000")
        sleep(2)  # Ждем 2 секунды для визуализации
        
        # Очищаем поле ввода
        input_field.clear()
        sleep(1)  # Ждем 1 секунду
        
        # Вводим новое значение "999"
        input_field.send_keys("999")
        sleep(2)  # Ждем 2 секунды для визуализации

    except Exception as ex:
        print(ex)
    finally:
        driver.quit()

# Запуск теста для Firefox
test_input_field("firefox")

# Запуск теста для Chrome
test_input_field("chrome")