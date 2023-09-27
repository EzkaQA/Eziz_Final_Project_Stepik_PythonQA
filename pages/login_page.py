from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        assert "login" in current_url, f"Wrong login link, login link should contain word 'login', but contains{current_url}"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is NOT displayed(found)"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is NOT displayed(found)"

    def register_new_user(self, email, password):
        registration_email_address = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_ADDRESS_FIELD)
        registration_email_address.send_keys(email)
        registration_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD)
        registration_password.send_keys(password)
        registration_password_confirm = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_FIELD)
        registration_password_confirm.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        register_button.click()
