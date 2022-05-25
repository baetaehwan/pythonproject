<<<<<<< HEAD
import cx_Oracle            

conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()


cursor.execute("drop table fruit")
cursor.execute("create table fruit(product varchar2(10), stock number(3),price number(5),receive number(8),sweet number(1))")
sql = "insert into fruit values(:1,:2,:3,:4,:5)"
product = input('과일명 >>>')
stock = input('수량 >>> ')
price = input('가격 >>> ')
receive = input('입고일자 >>> ')
sweet = input('당도 >>> ')
data = (product,int(stock),int(price),int(receive),int(sweet))
cursor.execute(sql,data)

squ1 = ""
cursor.close()
conn.commit()
=======
import cx_Oracle            

conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()


cursor.execute("drop table fruit")
cursor.execute("create table fruit(product varchar2(10), stock number(3),price number(5),receive number(8),sweet number(1))")
sql = "insert into fruit values(:1,:2,:3,:4,:5)"
product = input('과일명 >>>')
stock = input('수량 >>> ')
price = input('가격 >>> ')
receive = input('입고일자 >>> ')
sweet = input('당도 >>> ')
data = (product,int(stock),int(price),int(receive),int(sweet))
cursor.execute(sql,data)

squ1 = ""
cursor.close()
conn.commit()
>>>>>>> a08219a64da9ddeffedfcdc30de2ca7afe38677f
conn.close()