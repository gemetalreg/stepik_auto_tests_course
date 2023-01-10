from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

try:

    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button_submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_submit.click()

    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)

    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    f = math.log(abs(12*math.sin(int(x.text))))

    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input.send_keys(str(f))

    captcha_button_submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    captcha_button_submit.click()


finally:
    time.sleep(30)
    browser.quit()