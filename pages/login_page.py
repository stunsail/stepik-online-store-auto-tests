from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        registration_email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        registration_email_field.send_keys(email)
        registration_password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        registration_password_field.send_keys(password)
        registration_confirm_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD)
        registration_confirm_password.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
        
        
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.find("login") !=-1, "Login url is incorrect"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"
