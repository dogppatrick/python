import mysql.connector as mysql
from mysql.connector import errorcode
config = {"database": "db_01", "user": "sql_python", "password": "python"}


con1 = False
try:
    con1 = mysql.connect(**config)
    print("DB well opened")
except mysql.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("acc or password error")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("DB no find")
    else:
        print("ERROR")
finally:
    if con1:
        con1.close()
