from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

#проверка поиска числами.Вставляет случайное число от 1 до 20 и тыкает кнопку "Поиск"
link = "https://cosced.ru/"

try:
    browser = webdriver.Firefox()
    browser.get(link)
    input1 = browser.find_element(By.CLASS_NAME, "search-field")
    input1.send_keys (str(random.randint(1, 20)))
    button = browser.find_element(By.CSS_SELECTOR, "#search-2 > form > input")
    button.click()
       
finally:
    time.sleep(5)
    browser.quit()

