import pyodbc
import json


def isContact(student_num):
    with open("config.json") as config:
        close_contact_db_config = json.load(config)["selfreportDB"]
        server = close_contact_db_config["server"]
        database = close_contact_db_config["database"]
        username = close_contact_db_config["username"]
        password = close_contact_db_config["password"]
        driver = close_contact_db_config["driver"]
        with pyodbc.connect(
                'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password) as conn:
            with conn.cursor() as cursor:
                cursor.execute("select studentNum from close_contact where studentNum LIKE " + str(student_num))
                row = cursor.fetchone()
                return row != None


