
from src.connectDAO.connectDAO import ConnectDAO

import random


class HelperDB(object):
    def __init__(self):
        self.connect = ConnectDAO()

    def get_random_user_from_DB(self, sql, qty=None):
        if not qty:
            qty = 1

        result = self.connect.execute_SELECT(sql)
        return random.sample(result, qty)

    def get_user(self, sql):
        return self.connect.execute_SELECT(sql)
