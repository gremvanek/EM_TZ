from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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