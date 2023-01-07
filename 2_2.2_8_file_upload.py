from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_first_name = browser.find_element(By.CSS_SELECTOR, "input[required][name='firstname']")
    input_first_name.send_keys("Andrei")

    input_last_name = browser.find_element(By.CSS_SELECTOR, "input[required][name='lastname']")
    input_last_name.send_keys("Molchanov")

    input_email = browser.find_element(By.CSS_SELECTOR, "input[required][name='email']")
    input_email.send_keys("random@gmail.com")

    file_upload = browser.find_element(By.CSS_SELECTOR, "#file")
    
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(cur_dir, "file.txt")
    file_upload.send_keys(file_path)
 
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
