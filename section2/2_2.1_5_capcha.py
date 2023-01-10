from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    img_treasure = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = img_treasure.get_attribute("valuex")
    f = math.log(abs(12*math.sin(int(x))))

    input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_answer.send_keys(str(f))

    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot_checkbox.click()

    robots_radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robots_radio.click()

    submit_btn = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
