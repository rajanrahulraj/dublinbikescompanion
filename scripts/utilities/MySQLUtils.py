import mysql.connector
from scripts.constants import app_constants


class DBUtils:
    def __init__(self):
        self.db = mysql.connector.connect(
            host=app_constants.DB.HOST,
            user=app_constants.DB.USER,
            password=app_constants.DB.PASSWORD,
            port=app_constants.DB.PORT,
            database=app_constants.DB.DATABASE
        )

    def __del__(self):
        self.db.close()

    def execute_query(self, query):
        try:
            cursor = self.db.cursor()
            cursor.execute(query)
            self.db.commit()
        except Exception as e:
            print(str(e))
