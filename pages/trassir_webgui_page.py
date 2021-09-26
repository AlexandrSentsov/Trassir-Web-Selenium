from .login_page import LoginPage
from .locators import LoginPageLocators
from .locators import TrassirWebguiPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TrassirWebguiPage(LoginPage):

    def webgui_page_elements(self):
        assert self.is_element_present(*TrassirWebguiPageLocators.SETTINGS), "Settings is not presented"
        assert self.is_element_present(*TrassirWebguiPageLocators.TEMPLATE_1), "Template_1 is not presented"
        assert self.is_element_present(*TrassirWebguiPageLocators.TEMPLATE_4), "Template_4 is not presented"
        assert self.is_element_present(*TrassirWebguiPageLocators.TEMPLATE_9), "Template_9 is not presented"
        assert self.is_element_present(*TrassirWebguiPageLocators.TEMPLATE_16), "Template_16 is not presented"
        assert self.is_element_present(*TrassirWebguiPageLocators.TEMPLATE_25), "Template_25 not presented"
        assert self.is_element_present(*TrassirWebguiPageLocators.QUICKSEARCH), "Quicksearch not presented"
        assert self.is_element_present(*TrassirWebguiPageLocators.CURRENT_USER), "Current user not presented"
        assert self.is_element_present(*TrassirWebguiPageLocators.LOGOUT_BUTTON), "Logout button not presented"

    def logout(self, browser):
        WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((TrassirWebguiPageLocators.LOGOUT_BUTTON))
        ).click()
        login_form = WebDriverWait(browser, 30).until(
            EC.text_to_be_present_in_element((LoginPageLocators.LANGUAGES_LIST), 'English'))
        assert login_form != "True", "logout error"

    def current_user(self, browser):

        current_user = WebDriverWait(browser, 30).until(
            EC.text_to_be_present_in_element((TrassirWebguiPageLocators.CURRENT_USER), 'admin'))
        assert current_user != "admin", "The panel displays another user"