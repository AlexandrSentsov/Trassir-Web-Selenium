from .pages.trassir_webgui_page import TrassirWebguiPage
import pytest


@pytest.mark.need_to_test
def test_webgui_page_elements(browser):
    link = "https://172.16.14.151:8080/webgui/"
    page = TrassirWebguiPage(browser, link)
    page.open()
    page.autorization(browser, "admin", "12345")
    page.webgui_page_elements()

@pytest.mark.need_to_test
def test_logout(browser):
    link = "https://172.16.14.151:8080/webgui/"
    page = TrassirWebguiPage(browser, link)
    page.open()
    page.autorization(browser, "admin", "12345")
    page.logout(browser)

@pytest.mark.need_to_test
def test_current_user(browser):
    link = "https://172.16.14.151:8080/webgui/"
    page = TrassirWebguiPage(browser, link)
    page.open()
    page.autorization(browser, "admin", "12345")
    page.current_user(browser)