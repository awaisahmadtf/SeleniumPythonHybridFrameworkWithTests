from pagesobject.AccountCreationSuccessPage import AccountCreationSuccessPage
from pagesobject.BasePage import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    first_name_field_id = "input-firstname"
    last_name_field_id = "input-lastname"
    email_address_field_id = "input-email"
    telephone_field_id = "input-telephone"
    password_field_id = "input-password"
    confirm_password_field_id = "input-confirm"
    agree_field_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    yes_radio_button_xpath = "//label[normalize-space()='Yes']"
    duplicate_email_warning_message_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    privacy_policy_warning_message_xpath = "//div[@id='account-register']/div"
    first_name_warning_message_xpath = "//input[@id='input-firstname']/following-sibling::div"
    last_name_warning_message_xpath = "//input[@id='input-lastname']/following-sibling::div"
    email_warning_message_xpath = "//input[@id='input-email']/following-sibling::div"
    telephone_warning_message_xpath = "//input[@id='input-telephone']/following-sibling::div"
    password_warning_message_xpath = "//input[@id='input-password']/following-sibling::div"

    def enter_first_name(self, first_name):
        self.type_text(first_name, "first_name_field_id", self.first_name_field_id)

    def enter_last_name(self, last_name):
        self.type_text(last_name, "last_name_field_id", self.last_name_field_id)

    def enter_email_address(self, email_address):
        self.type_text(email_address, "email_address_field_id", self.email_address_field_id)

    def enter_telephone(self, telephone):
        self.type_text(telephone, "telephone_field_id", self.telephone_field_id)

    def enter_password(self, password):
        self.type_text(password, "password_field_id", self.password_field_id)

    def enter_confirm_password(self, confirm_password):
        self.type_text(confirm_password, "confirm_password_field_id", self.confirm_password_field_id)

    def select_agree_checkbox(self):
        self.element_click("agree_field_name", self.agree_field_name)

    def click_on_continue_button(self):
        self.element_click("continue_button_xpath", self.continue_button_xpath)
        return AccountCreationSuccessPage(self.driver)

    def select_yes_radio_button(self):
        self.element_click("yes_radio_button_xpath", self.yes_radio_button_xpath)

    def retrieve_duplicate_email_warning_message(self):
        return self.retrieve_element_text("duplicate_email_warning_message_xpath",
                                          self.duplicate_email_warning_message_xpath)

    def retrieve_privacy_policy_warning_message(self):
        return self.retrieve_element_text("privacy_policy_warning_message_xpath",
                                          self.privacy_policy_warning_message_xpath)

    def retrieve_first_name_warning_message(self):
        return self.retrieve_element_text("first_name_warning_message_xpath", self.first_name_warning_message_xpath)

    def retrieve_last_name_warning_message(self):
        return self.retrieve_element_text("last_name_warning_message_xpath", self.last_name_warning_message_xpath)

    def retrieve_email_warning_message(self):
        return self.retrieve_element_text("email_warning_message_xpath", self.email_warning_message_xpath)

    def retrieve_telephone_warning_message(self):
        return self.retrieve_element_text("telephone_warning_message_xpath", self.telephone_warning_message_xpath)

    def retrieve_password_warning_message(self):
        return self.retrieve_element_text("password_warning_message_xpath", self.password_warning_message_xpath)

    def register_an_account(self, first_name, last_name, email_address, telephone, password, confirm_password,
                            subscribe_yes_or_no, privacy_select_yes):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email_address(email_address)
        self.enter_telephone(telephone)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        if subscribe_yes_or_no.__eq__("yes"):
            self.select_yes_radio_button()
        if privacy_select_yes.__eq__("yes"):
            self.select_agree_checkbox()
        return self.click_on_continue_button()

    def verify_all_warnings(self, privacy_policy_warning, first_name_warning, last_name_warning, email_warning,
                            telephone_warning, password_warning):
        actual_privacy_policy_warning = self.retrieve_privacy_policy_warning_message()
        actual_first_name_warning = self.retrieve_first_name_warning_message()
        actual_last_name_warning = self.retrieve_last_name_warning_message()
        actual_email_warning = self.retrieve_email_warning_message()
        actual_telephone_warning = self.retrieve_telephone_warning_message()
        actual_password_warning = self.retrieve_password_warning_message()

        waring_status = False
        if actual_privacy_policy_warning.__contains__(privacy_policy_warning):
            if actual_first_name_warning.__eq__(first_name_warning):
                if actual_last_name_warning.__eq__(last_name_warning):
                    if actual_email_warning.__eq__(email_warning):
                        if actual_telephone_warning.__eq__(telephone_warning):
                            if actual_password_warning.__eq__(password_warning):
                                waring_status = True

        return waring_status
