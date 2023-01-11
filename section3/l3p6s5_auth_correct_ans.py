import pytest, time, math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(30)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url', ["https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"])
def test_auth(browser, url):
    
    link = url
    browser.get(link)

    login_btn = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".navbar__auth_login")))
    login_btn.click()

    my_email=""
    my_pass=""

    email_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name=\"login\"]")))
    email_input.send_keys(my_email)

    pass_input = browser.find_element(By.CSS_SELECTOR, "input[name=\"password\"]")
    pass_input.send_keys(my_pass)

    submit_btn = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sign-form__btn")))
    submit_btn.click()


    textarea_ans = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea.ember-text-area")))
    answer = math.log(int(time.time()))
    textarea_ans.send_keys(str(answer))

    text_submit_btn = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
    text_submit_btn.click()

    hint = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
     
    if hint.text != "Correct!": 
        with open("text.txt", "at") as f:
            f.write(hint.text)
