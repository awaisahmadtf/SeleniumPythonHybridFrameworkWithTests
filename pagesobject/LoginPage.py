
from pagesobject.BasePage import BasePage
from pagesobject.AccountPage import AccountPage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    email_address_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    wrong_credentials__warning_message_xpath = "//div[@class='alert alert-danger alert-dismissible']"

    def enter_email_address(self, email_address):
        self.type_text(email_address, "email_address_field_id", self.email_address_field_id)

    def enter_password(self, password):
        self.type_text(password, "password_field_id", self.password_field_id)

    def click_on_login_button(self):
        self.element_click("login_button_xpath", self.login_button_xpath)
        return AccountPage(self.driver)

    def retrieve_wrong_credentials_warning_message(self):
        return self.retrieve_element_text("wrong_credentials__warning_message_xpath", self.wrong_credentials__warning_message_xpath)

    def login_with_given_credentials(self, email_address, password):
        self.enter_email_address(email_address)
        self.enter_password(password)
        return self.click_on_login_button()
