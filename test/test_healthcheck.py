from test.BaseTest import BaseTest

import logging

import pytest

class Test_helathcheck(BaseTest):

    @pytest.mark.healthcheck
    def test_healthcheck(self):
        logging.debug("Hello world!!!")
        assert True

    @pytest.mark.tcid00
    def test_check_db_connection(self):
        get_random_user = self.HelperDB.get_random_user_from_DB(self.SQL.SQL_get_random_user(), 20)
        logging.info(get_random_user)
        assert get_random_user is not None

    @pytest.mark.tcid01
    def test_get_user(self):
        email = "testuser_rxjmu@gmail.com"
        result = self.HelperDB.get_user(self.SQL.SQL_get_user_by_email(email))
        assert result[0]['email'] == email, f"Expected result: {email} but DB returned: {result[0]['email']}"
