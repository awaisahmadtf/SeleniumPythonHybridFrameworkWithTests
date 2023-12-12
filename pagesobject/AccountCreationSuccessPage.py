from pagesobject.BasePage import BasePage


class AccountCreationSuccessPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    account_creation_success_message_xpath = "//div[@id='content']/h1"

    def retrieve_account_creation_success_message(self):
        return self.retrieve_element_text("account_creation_success_message_xpath",
                                          self.account_creation_success_message_xpath)
