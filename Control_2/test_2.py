from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from configuration import *

def test_calculator_form(chrome_browser): 
    chrome_browser.get(URL_2)

    # Заполняем поле задержки
    delay_input = chrome_browser.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys(45) 

    # Находим и кликаем на кнопки калькулятора
    chrome_browser.find_element(By.XPATH, "//span[text() = '7']").click()
    chrome_browser.find_element(By.XPATH, "//span[text() = '+']").click()
    chrome_browser.find_element(By.XPATH, "//span[text() = '8']").click()
    chrome_browser.find_element(By.XPATH, "//span[text() = '=']").click()

    # Ожидаем, что текст результата появится на экране
    result = WebDriverWait(chrome_browser, 46).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )

    # Получаем текст результата
    result_text = chrome_browser.find_element(By.CLASS_NAME, "screen").text

    # Проверяем, что результат равен 15
    assert result_text == "15", f"Expected result to be '15', but got '{result_text}'"  