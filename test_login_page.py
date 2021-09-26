from .pages.login_page import LoginPage
from .pages.locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.need_to_test
def test_login_form_elements(browser):
    link = "https://172.16.14.151:8080/webgui/"
    page = LoginPage(browser, link)
    page.open()
    page.login_form_elements()

@pytest.mark.need_to_test
@pytest.mark.parametrize('password', ["12345"])
def test_autorization(browser, password):
    link = "https://172.16.14.151:8080/webgui/"
    page = LoginPage(browser, link)
    page.open()
    username = "admin"
    page.autorization(browser, username, password)

@pytest.mark.need_to_test
@pytest.mark.parametrize('password', ["", " ", "1337", "admin", "admin1337", "админ", "."])
def test_wrong_login_password(browser,password):
    link = "https://172.16.14.151:8080/webgui/"
    page = LoginPage(browser, link)
    page.open()
    username = "admin"
    page.autorization(browser, username, password)
    login_error = WebDriverWait(browser, 30).until(
        EC.text_to_be_present_in_element((LoginPageLocators.INTERNAL_SERVER_ERROR), 'Internal server error'))
    assert login_error != "True", "Error login message not found"


@pytest.mark.need_to_test
def test_languages_list(browser):
    link = "https://172.16.14.151:8080/webgui/"
    page = LoginPage(browser, link)
    page.open()
    page.languages_list(browser)


@pytest.mark.need_to_test
def test_guest_can_see_all_languages(browser):
    link = "https://172.16.14.151:8080/webgui/"
    page = LoginPage(browser, link)
    page.open()
    page.language_switching(browser)
