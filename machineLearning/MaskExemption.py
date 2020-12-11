import pyodbc
import json


def hasMaskExemption(student_num):
    with open("config.json") as config:
        mask_exemption_db_config = json.load(config)["maskexpemtionDB"]
        server = mask_exemption_db_config["server"]
        database = mask_exemption_db_config["database"]
        username = mask_exemption_db_config["username"]
        password = mask_exemption_db_config["password"]
        driver = mask_exemption_db_config["driver"]
        with pyodbc.connect(
                'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password) as conn:
            with conn.cursor() as cursor:
                cursor.execute("select studentNum from exempt where studentNum LIKE " + str(student_num))
                row = cursor.fetchone()
                return row != None

