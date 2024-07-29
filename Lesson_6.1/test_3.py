from selenium.webdriver.common.by import By
from configuration import*

def test_shop_form(chrome_browser):
    chrome_browser.get(URL_3)

    # Вводим имя пользователя и пароль
    chrome_browser.find_element(By.ID, "user-name").send_keys("standard_user")
    chrome_browser.find_element(By.ID, "password").send_keys("secret_sauce")
    chrome_browser.find_element(By.ID, "login-button").click()

    # Добавляем товары в корзину
    chrome_browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    chrome_browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    chrome_browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # Переходим в корзину и начинаем оформление заказа
    chrome_browser.find_element(By.ID, "shopping_cart_container").click()
    chrome_browser.find_element(By.ID, "checkout").click()

    # Вводим данные для оформления заказа
    chrome_browser.find_element(By.ID, "first-name").send_keys("Evgen")
    chrome_browser.find_element(By.ID, "last-name").send_keys("Voronov")
    chrome_browser.find_element(By.ID, "postal-code").send_keys("601500")
    chrome_browser.find_element(By.ID, "continue").click()

    # Получаем итоговую сумму
    total_price = chrome_browser.find_element(By.CLASS_NAME, 'summary_total_label')
    total = total_price.text.strip().replace("Total: $", "")

    expected_total = "58.29"

    # Проверяем, что итоговая сумма равна $58.29
    assert total == expected_total, f"Expected total to be {expected_total}, but got {total}"
    print("Итоговая сумма равна $58.29")  # Выводим сообщение в случае успешного выполнения