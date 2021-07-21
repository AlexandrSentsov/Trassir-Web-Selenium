from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

@pytest.fixture
def browser():
    link = "https://localhost:8080/webgui/"
    browser = webdriver.Chrome()
    browser.get(link)
    return browser

def test_login_logout(browser):
    browser.find_element_by_id("details-button").click()
    browser.find_element_by_id("proceed-link").click()
    browser.find_element_by_id("login-username").send_keys("admin")
    browser.find_element_by_css_selector("#login-dialog > div > form > div:nth-child(4) > div > div > input").send_keys("12345")
    browser.find_element_by_css_selector(".text-right .btn").click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".logout > div:nth-child(1)"))
    ).click()
    browser.quit()

def test_list_languages(browser):
    browser.find_element_by_id("details-button").click()
    browser.find_element_by_id("proceed-link").click()
    browser.find_element_by_id("login-dialog-language-selector-button").click()
    languages = []
    for i in range(1, 9):
        language = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div/form/div[6]/div/div/ul/li[" + str(i) + "]/a").text
        languages.append(language.lstrip())
    assert languages == ['English', 'Français', 'ქართული', 'Русский', 'Türkçe', 'Українська', '简体中文（jiǎntǐ zhōngwén）',
                         '繁体中文(fántǐ zhōngwén)'], "error in the list of languages "
    browser.quit()
