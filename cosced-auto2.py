from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Тест заполняет форму обратной связи и нажимает "Отправить"
link = "https://cosced.ru/tutoring/services-for-finding-specialists/"


try:
    browser = webdriver.Firefox()
    browser.get(link)
    input1 = browser.find_element(By.ID, "author")
    input1.send_keys ("Евгений")
    input2 = browser.find_element(By.ID, "email")
    input2.send_keys ("ivan.malaf@rambler.ru")
    input3 = browser.find_element(By.ID, "url")
    input3.send_keys ("loh.ru")
    button = browser.find_element(By.ID,"submit")
    button.click()
    

finally:
    time.sleep(10)
    browser.quit()
