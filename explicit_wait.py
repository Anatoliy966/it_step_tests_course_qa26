# lessons_12_1__05.10.2023

# Явное ожидание

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome() # Создаем экземпляр нашего драйвера
# Говорим WebDriver'у искать каждый элемент на протяжении 2 секунд. Прописываем один раз.

browser.implicitly_wait(2) # это  неявное ожидание

try:
    print("Browser Start!")
    browser.get("https://casenik.com.ua/user/login") # Переходим на сайт - вход
    time.sleep(2)
    email_filed = browser.find_element(By.XPATH, "//input[@id='email']")
    email_filed.send_keys("gegoj75947@ipniel.com")
    time.sleep(2)
    password_filed = browser.find_element(By.XPATH, "//input[@id='pasword']")
    password_filed.send_keys("Qwerty22")
    time.sleep(2)
    login_button = browser.find_element(By.XPATH, "//button[@class='btn button-gen']").click() # нажали кнопку Вход
    time.sleep(5)

    # Эта конструкция - это и есть реализация нашего явного ожидания:
    # 32 - это секунды (на нашем сайте оповещение о регистрации исчезает ч/з 30 сек.)
    # метод .until_not на протяжении указанного времени проверяет наличие или отсутствие данного элемента.
    # .until_not - ожидаем, когда элемент исчезнет.
    # есть метод просто .until - это значит, что ожидается, что элемент появится.
    message = WebDriverWait(browser, 32).until_not(
        # EC.element_to_be_clickable((By.XPATH, "//div[@class = 'alert alert-success']")) # это случай, когда:
        # появляется кнопка, но некоторое время она не активна. Эсли попытаемся на нее нажать - будет ошибка.
        # Надо просто подождать, когда она станет активной.
        EC.visibility_of_element_located((By.XPATH, "//div[@class = 'alert alert-success']"))
    )
    # Если поставим 29 сек., скрипт упадет

    time.sleep(5)
finally:
    browser.quit() # закрываем браузер
    print("Browser quit")