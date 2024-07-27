from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

def login_test(browser):
    # Инициализация драйвера
    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError("Поддерживаются только 'firefox' и 'chrome'")

    try:
        driver.get("https://the-internet.herokuapp.com/login")
        
        # Вводим имя пользователя
        input_name = driver.find_element(By.ID, "username").send_keys("tomsmith")
        sleep(1)

        # Вводим пароль
        input_pass = driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        sleep(1)

        # Нажимаем кнопку входа
        button = driver.find_element(By.TAG_NAME, "button").click()
        sleep(2)

    except Exception as ex:
        print(ex)
    finally:
        driver.quit()

# Запуск теста для Firefox
login_test("firefox")

# Запуск теста для Chrome
login_test("chrome")