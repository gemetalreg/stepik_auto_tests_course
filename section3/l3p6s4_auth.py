import pytest, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

def test_auth(browser):
    link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)

    login_btn = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".navbar__auth_login")))
    login_btn.click()

    my_email=""
    my_pass=""

    email_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name=\"login\"]")))
    email_input.send_keys(my_email)

    pass_input = browser.find_element(By.CSS_SELECTOR, "input[name=\"password\"]")
    pass_input.send_keys(my_pass)

    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
    submit_btn.click()

    time.sleep(10)