import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from utilities import ReadConfigurations


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test",attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def setup_and_teardown(request):
    global driver
    browser = ReadConfigurations.read_configuration("basic info", "browser")
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    else:
        print("Provide a valid browser")
    driver.maximize_window()
    driver.get(ReadConfigurations.read_configuration("basic info", "url"))
    request.cls.driver = driver
    yield
    driver.quit()
