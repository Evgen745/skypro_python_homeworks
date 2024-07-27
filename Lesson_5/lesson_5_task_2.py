from selenium import webdriver
from time import sleep

def test_dynamic_button(browser):
    # Инициализация драйвера
    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError("Поддерживаются только 'firefox' и 'chrome'")

    try:
        count = 0
        driver.get("http://uitestingplayground.com/dynamicid")

        # Находим кнопку один раз (для Firefox)
        blue_button = driver.find_element("xpath", '//button[text()="Button with Dynamic ID"]')

        # Кликаем по кнопке и затем повторяем это 3 раза
        for _ in range(3):
            blue_button.click()  # Клик по кнопке
            count += 1  # Увеличиваем счетчик
            sleep(2)  # Ждем 2 секунды
            print(count)  # Выводим счетчик

    except Exception as ex:
        print(ex)
    finally:
        driver.quit()

# Запуск теста для Firefox
test_dynamic_button("firefox")

# Запуск теста для Chrome
test_dynamic_button("chrome")