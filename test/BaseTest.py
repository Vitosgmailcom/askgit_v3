import pytest

from src.Helpers.helperDB import HelperDB
from src.SQL.SQL import SQL_statements

class BaseTest:
    SQL: SQL_statements
    HelperDB: HelperDB

    @pytest.fixture(autouse=True)
    def setup(self, request):
        request.cls.SQL = SQL_statements()
        request.cls.HelperDB = HelperDB()




