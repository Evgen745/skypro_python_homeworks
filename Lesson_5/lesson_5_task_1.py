from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Инициализация драйверов
chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    # Открытие страницы
    chrome.get("https://the-internet.herokuapp.com/add_remove_elements/")
    firefox.get("https://the-internet.herokuapp.com/add_remove_elements/")

    for _ in range(5):
        # Нажатие на кнопку "Add Element"
        chrome.find_element(By.XPATH, '//button[text()="Add Element"]').click()
        firefox.find_element(By.XPATH, '//button[text()="Add Element"]').click()
        sleep(1)

        # Получение всех кнопок "Delete"
        chrome_delete_buttons = chrome.find_elements(By.XPATH, '//button[text()="Delete"]')
        firefox_delete_buttons = firefox.find_elements(By.XPATH, '//button[text()="Delete"]')

        # Вывод размера списка кнопок "Delete"
        print(f"размер списка кнопок Delete в Chrome: {len(chrome_delete_buttons)}")
        print(f"размер списка кнопок Delete в Firefox: {len(firefox_delete_buttons)}")

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
    firefox.quit()