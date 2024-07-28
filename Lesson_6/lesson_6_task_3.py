from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_loading_images(browser):
    # Инициализация драйвера
    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError("Поддерживаются только 'firefox' и 'chrome'")

    wait = WebDriverWait(driver, 40, 0.1)

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
        
        # Ожидаем, что текст 'Done!' появится в элементе с id 'text'
        wait.until(EC.text_to_be_present_in_element((By.ID, "text"), 'Done!'))
        
        # Извлекаем атрибут 'src' у элемента с id 'award'
        get_attribute = driver.find_element(By.ID, "award").get_attribute("src")
        print(get_attribute)

    except Exception as ex:
        print(ex)
    finally:
        driver.quit()

# Запуск теста для Firefox
test_loading_images("firefox")

# Запуск теста для Chrome
test_loading_images("chrome")