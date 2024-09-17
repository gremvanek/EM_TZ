from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настройка драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager("114.0.5735.90").install()))

try:
    # Переход на сайт
    driver.get("https://www.saucedemo.com/")
    
    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    
    # Явное ожидание для кнопки логина
    wait = WebDriverWait(driver, 10)
    login_button = wait.until(EC.presence_of_element_located((By.ID, "login-button")))
    login_button.send_keys(Keys.RETURN)
    
    # Выбор товара и добавление в корзину
    time.sleep(5)  # Время для прогрузки элементов сайта
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()  # Поиск и добавление товара в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()  # Переход в корзину
    time.sleep(5)  # Время для прогрузки элементов сайта
    
    # Проверка наличия товара в корзине
    assert "Sauce Labs Backpack" in driver.page_source, "Товар не найден в корзине!"
    
    # Оформление покупки
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    
    # Завершение покупки
    driver.find_element(By.ID, "finish").click()
    
    # Проверка успешного завершения
    assert "Thank you for your order!" in driver.page_source, "Покупка не завершена!"
    print("Тест успешно завершен!")
    
finally:
    driver.quit()