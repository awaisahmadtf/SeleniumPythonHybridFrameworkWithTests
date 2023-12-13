

import allure
import pytest
from pagesobject.HomePage import HomePage
from tests.BaseTest import BaseTest
from utilities import ExcelReader


class TestLogin(BaseTest):

    @pytest.mark.parametrize("email_address, password", ExcelReader.get_data_from_excel("ExcelFiles/TestFile.ods", "LoginTest"))
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_login_with_valid_credentials(self, email_address, password):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        # account_page = login_page.login_with_given_credentials("testawais@test.com", "12345")
        account_page = login_page.login_with_given_credentials(email_address, password)
        assert account_page.display_status_of_edit_your_account_info_opt()

    @allure.severity(allure.severity_level.MINOR)
    def test_login_without_entering_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_with_given_credentials("", "")
        expected_warning = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_wrong_credentials_warning_message().__contains__(expected_warning)

    def test_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_with_given_credentials("testawais@test.com", "1")
        expected_warning = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_wrong_credentials_warning_message().__contains__(expected_warning)

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_with_invalid_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_with_given_credentials(self.generate_email_time_stamp(), "1")
        expected_warning = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_wrong_credentials_warning_message().__contains__(expected_warning)


