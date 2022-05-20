import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()
cursor.execute("select * from emp")

# print(cursor)

for item in cursor:
    while True: 
        job = input('직업을 입력하세요 >>>').upper()
        
        if job == item[2]:
            name = 
            print(name)

conn.close()