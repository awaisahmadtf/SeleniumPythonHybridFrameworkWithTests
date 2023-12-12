import datetime

import pytest


@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class BaseTest:

    def generate_email_time_stamp(self):
        timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "ali" + timestamp + "@test.com"
