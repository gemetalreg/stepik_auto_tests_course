from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num = browser.find_element(By.CSS_SELECTOR, "#input_value")
    f = math.log(abs(12*math.sin(int(num.text))))

    input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_answer.send_keys(str(f))

    submit_btn = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_btn)

    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot_checkbox.click()

    robots_radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robots_radio.click()

    
    submit_btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
