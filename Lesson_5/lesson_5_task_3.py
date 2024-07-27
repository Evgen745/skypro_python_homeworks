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
        driver.get("http://uitestingplayground.com/classattr")

        for _ in range(3):
            # Находим кнопку и кликаем по ней
            blue_button = driver.find_element("xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
            blue_button.click()
            sleep(2)  # Ждем 2 секунды, чтобы увидеть результат клика

            # Принимаем алерт
            driver.switch_to.alert.accept()

    except Exception as ex:
        print(ex)
    finally:
        driver.quit()

# Запуск теста для Firefox
test_dynamic_button("firefox")

# Запуск теста для Chrome
test_dynamic_button("chrome")

