sql = "select    ename, salary from employee"
sql = sql.replace(", ", ",")
sql_sp = sql.split(sep=" ")
while "" in sql_sp:
    sql_sp.remove("")

if sql_sp[0].lower() == "select":
    print("select")
    index_from = sql_sp.index("from")
    print(sql_sp[index_from+1])
    c = sql_sp[1].split(sep=",")
    for colum in c:
        print(colum)
else:
    print("error")

