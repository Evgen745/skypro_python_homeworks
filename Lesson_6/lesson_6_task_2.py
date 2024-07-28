from selenium import webdriver
from time import sleep

def test_text_input(browser):
    # Инициализация драйвера
    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError("Поддерживаются только 'firefox' и 'chrome'")

    try:
        driver.get("http://uitestingplayground.com/textinput")
        
        # Вводим текст в поле
        button_name = driver.find_element("id", "newButtonName").send_keys("SkyPro")
        sleep(2)  # Ждем 2 секунды для визуализации
        
        # Нажимаем кнопку для обновления имени
        confirm_button_name = driver.find_element("id", "updatingButton").click()
        sleep(2)  # Ждем 2 секунды после нажатия кнопки
        
        # Получаем текст обновленной кнопки
        new_button_name = driver.find_element("id", "updatingButton").text
        sleep(2)  # Ждем 2 секунды для визуализации
        
        print(new_button_name)  # Выводим новый текст кнопки

    except Exception as ex:
        print(ex)
    finally:
        driver.quit()

# Запуск теста для Firefox
test_text_input("firefox")

# Запуск теста для Chrome
test_text_input("chrome")