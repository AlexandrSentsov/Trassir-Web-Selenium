from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):

    def login_form_elements(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Login username is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password is not presented"
        assert self.is_element_present(*LoginPageLocators.LANGUAGES_LIST), "Languages list is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def autorization(self, browser, username, password):
        browser.find_element(*LoginPageLocators.LOGIN_USERNAME).send_keys(username)
        browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys(password)
        browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def languages_list(self, browser):
        browser.find_element(*LoginPageLocators.LANGUAGES_LIST).click()
        languages = []
        for i in range(1, 9):
            language = browser.find_element_by_xpath(
                "/html/body/div/div[2]/div/form/div[6]/div/div/ul/li[" + str(i) + "]/a").text
            languages.append(language.lstrip())
        assert languages == ['English', 'Français', 'ქართული', 'Русский', 'Türkçe', 'Українська', '简体中文（jiǎntǐ zhōngwén）',
                             '繁体中文(fántǐ zhōngwén)'], "error in the list of languages "

    def language_switching(self, browser):
        placeholders_list_username = ["Login", "Nom d'utilisateur", "სისტემაში შესვლა",  "Имя пользователя", "Kullanıcı adı", "Логін", "用户名：", "登入："]
        placeholders_list_passwords = ["Password", "Mot de passe", "პაროლი", "Пароль", "Parola", "Пароль", "密码：", "密碼："]
        for i in range(0, 8):
            current_language = browser.find_element(*LoginPageLocators.LANGUAGES_LIST_TEXT).text
            browser.find_element(*LoginPageLocators.LANGUAGES_LIST).click()
            browser.find_element_by_xpath("/html/body/div/div[2]/div/form/div[6]/div/div/ul/li[" + str(i + 1) + "]/a").click()
            time.sleep(1)
            username_placeholder = browser.find_element(*LoginPageLocators.LOGIN_USERNAME).get_attribute("placeholder")
            password_placeholder = browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).get_attribute("placeholder")
            assert username_placeholder != placeholders_list_username[i - 1] and password_placeholder != placeholders_list_passwords[i - 1], f'{current_language} language did not switch'
