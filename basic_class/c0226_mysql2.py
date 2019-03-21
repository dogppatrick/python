import mysql.connector as mysql
from mysql.connector import errorcode
config = {"database": "db_01", "user": "sql_python", "password": "python"}


con1 = False
try:
    con1 = mysql.connect(**config)
    # print("DB well opened")
    cursor = con1.cursor()
    sql_cmd = "select empno, ename, salary from emp where salary >= %(salary)s"
    # sql_cmd = "select empno, ename, salary from emp where salary >= %s"
    q_dict = {"salary": 50000}
    # salary_d = 50000
    cursor.execute(sql_cmd, q_dict)
    # cursor.execute(sql_cmd, (salary_d,))
    data_raw = cursor.fetchall()
    raw_c = cursor.rowcount
    print(raw_c)
    # print(data_raw)
    # for empno, ename in cursor:
    #     print(empno, ename)
    for data in data_raw:
        print(data)

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
