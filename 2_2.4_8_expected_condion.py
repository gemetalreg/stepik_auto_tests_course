from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math, time
try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()

    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    f = math.log(abs(12*math.sin(int(x.text))))

    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input.send_keys(str(f))

    captcha_button_submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    captcha_button_submit.click()
finally:
    time.sleep(30)

    browser.quit()