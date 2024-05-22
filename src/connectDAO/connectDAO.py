
import pymysql.cursors
import os
import dotenv
dotenv.load_dotenv()


class ConnectDAO:
    def __init__(self):
        pass

    def connect_DAO(self):
        connect = pymysql.connect(
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASS'],
            database=os.environ['DB_NAME'],
            port=int(os.environ['DB_PORT']),
            host=os.environ['DB_HOST']
        )
        return connect

    def execute_SELECT(self, sql):

        conn = self.connect_DAO()

        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()

            return result
