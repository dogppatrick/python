import mysql.connector as mysql
from mysql.connector import errorcode
config = {"database": "db_01", "user": "sql_python", "password": "python"}


con1 = False
try:
    con1 = mysql.connect(**config)
    cursor = con1.cursor()

    sql_ins = "insert into emp values (%s, %s, %s, %s, %s, %s, %s)"
    ins_data = (1011, "AAA", "2019-02-26", 80000, 400, "SA_REP", 1004)
    ins_data1 = (1021, "AAA", "2019-02-26", 80000, 400, "SA_REP", 1004)
    ins_data2 = (1031, "AAA", "2019-02-26", 80000, 400, "SA_REP", 1004)
    sql_upd = "update emp set salary=%s where empno=%s"
    upd_data = (95000, 1011)
    sql_cmd = "select empno, ename, salary from emp "
    sql_del = "delete from emp where empno = %s"
    empno = 1009
    q_dict = {"salary": 50000}
    cursor.execute(sql_del, (empno,))
    cursor.execute(sql_ins, ins_data1)
    cursor.execute(sql_ins, ins_data2)
    # cursor.execute(sql_upd, upd_data)
    con1.commit()
    cursor.execute(sql_cmd)
    data_raw = cursor.fetchall()
    raw_c = cursor.rowcount
    print(raw_c)
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
