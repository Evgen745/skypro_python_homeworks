import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_modal_window(browser):
    # Инициализация драйвера
    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError("Поддерживаются только 'firefox' и 'chrome'")

    try:
        driver.get("https://the-internet.herokuapp.com/entry_ad")

        wait = WebDriverWait(driver, 10)

        # Ожидаем появления модального окна
        modal_window = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal"))
        )

        # Ожидаем, что кнопка закрытия будет кликабельной
        close_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer"))
        )

        time.sleep(3)  # Ждем 3 секунды для визуализации модального окна

        close_button.click()  # Кликаем по кнопке закрытия
        time.sleep(2)  # Ждем 2 секунды после закрытия

    except Exception as ex:
        print(ex)
    finally:
        driver.quit()

# Запуск теста для Firefox
test_modal_window("firefox")

# Запуск теста для Chrome
test_modal_window("chrome")