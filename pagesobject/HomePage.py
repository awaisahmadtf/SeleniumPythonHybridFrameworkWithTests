
from pagesobject.LoginPage import LoginPage
from pagesobject.RegisterPage import RegisterPage
from pagesobject.Searchpage import SearchPage
from pagesobject.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    search_box_field_name = "search"
    search_button_xpath = "//button[contains(@class,'btn-default')]"
    my_account_drop_menu_xpath = "//span[normalize-space()='My Account']"
    login_option_link_text = "Login"
    register_option_link_text = "Register"

    def enter_product_into_search_box_field(self, product_name):
        self.type_text(product_name, "search_box_field_name", self.search_box_field_name)

    def click_on_search_button(self):
        self.element_click("search_button_xpath", self.search_button_xpath)
        return SearchPage(self.driver)

    def click_on_my_account_drop_menu(self):
        self.element_click("my_account_drop_menu_xpath", self.my_account_drop_menu_xpath)

    def select_login_option(self):
        self.element_click("login_option_link_text", self.login_option_link_text)
        return LoginPage(self.driver)

    def select_register_option(self):
        self.element_click("register_option_link_text", self.register_option_link_text)
        return RegisterPage(self.driver)

    def search_for_a_product(self, product_name):
        self.enter_product_into_search_box_field(product_name)
        return self.click_on_search_button()

    def navigate_to_login_page(self):
        self.click_on_my_account_drop_menu()
        return self.select_login_option()

    def navigate_to_register_page(self):
        self.click_on_my_account_drop_menu()
        return self.select_register_option()
