import datetime
import pytest
from selenium.webdriver.common.by import By
from pagesobject.AccountCreationSuccessPage import AccountCreationSuccessPage
from pagesobject.HomePage import HomePage
from pagesobject.RegisterPage import RegisterPage
from tests.BaseTest import BaseTest
from utilities import ExcelReader


class TestRegister(BaseTest):
    def test_create_account_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_creation_success_page = register_page.register_an_account(ExcelReader.get_cell_data("ExcelFiles/TestFile.ods", "RegisterTest", "2","1"),
                                                                          ExcelReader.get_cell_data("ExcelFiles/TestFile.ods", "RegisterTest", "2","2"),
                                                                          self.generate_email_time_stamp(),
                                                                          ExcelReader.get_cell_data("ExcelFiles/TestFile.ods", "RegisterTest", "2","3"),
                                                                          "12345", "12345", "no", "yes")
        expected_text = "Your Account Has Been Created!"
        assert account_creation_success_page.retrieve_account_creation_success_message().__eq__(expected_text)

    def test_create_account_with_all_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_creation_success_page = register_page.register_an_account("Ali", "Ahmad",
                                                                          self.generate_email_time_stamp(),
                                                                          "12354862574", "12345", "12345", "yes", "yes")
        expected_text = "Your Account Has Been Created!"
        assert account_creation_success_page.retrieve_account_creation_success_message().__eq__(expected_text)

    def test_create_account_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("Ali", "Ahmad", "testawais@test.com", "12354862574", "12345", "12345", "yes",
                                          "yes")
        expected_warning = "Warning: E-Mail Address is already registered!"
        register_page.retrieve_duplicate_email_warning_message().__contains__(expected_warning)

    def test_create_account_without_entering_any_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("", "", "", "", "", "", "no", "no")

        privacy_policy_warning = "Warning: You must agree to the Privacy Policy!"
        first_name_warning = "First Name must be between 1 and 32 characters!"
        last_name_warning = "Last Name must be between 1 and 32 characters!"
        email_warning = "E-Mail Address does not appear to be valid!"
        telephone_warning = "Telephone must be between 3 and 32 characters!"
        password_warning = "Password must be between 4 and 20 characters!"

        register_page.verify_all_warnings(privacy_policy_warning, first_name_warning, last_name_warning, email_warning,
                                          telephone_warning, password_warning)


