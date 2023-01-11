from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest, time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket(browser):
    browser.get(link)
    try:
        browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket[type='submit']")
        time.sleep(30)
    except NoSuchElementException:
        assert False, "Didn't find add to basket button"

    