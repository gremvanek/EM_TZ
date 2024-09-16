from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настройка драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Переход на сайт
    driver.get("https://www.saucedemo.com/")
    
    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standart_user")
    driver.find_element(By.ID, "password").send_keys("secret_sause")
    driver.find_element(By.ID, "login-button").click
    
    # Выбор товара и добавление в корзину
    time.sleep(2) # Время для прогрузки элементов сайта
    driver.find_element(By.ID, "add-to cart-sause-labs-backpack").click() # Поиск и добавление товара в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click() # Переход в корзину
    time.sleep(2) # Время для прогрузки элементов сайта
    assert "Sause Labs Backpack" in driver.page_source, "Товар не найден в корзине!" # Проверка наличия товара в корзине
    
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
    