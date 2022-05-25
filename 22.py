<<<<<<< HEAD
import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()
# cursor.execute("create table fruit(product varchar2(100), stock number(3),price number(5),receive number(8),sweet number(1))")


while True:
    choice=input('''
다음 중에서 하실 일을 골라주세요 :
I - 입력 \t S - 판매 \t L- 재고 리스트 \t D-삭제 \t Q-종료
>>> ''').upper()
    if choice == 'I':
        sql = "insert into fruit values(:1,:2,:3,:4,:5)"
        cursor.execute("select * from fruit")
        product = input('과일명 >>>')
        stock = input('수량 >>> ')
        price = input('가격 >>> ')
        receive = input('입고일자 >>> ')
        sweet = input('당도 >>> ')
        data = (product,int(stock),int(price),int(receive),int(sweet))
        cursor.execute(sql,data)
        cursor.close()
        conn.commit()
        conn.close()

    elif choice == 'S':
        sql = "update fruit set stock = stock -sold where product = name"
        name = input('과일명 >>>')
        sold = input('수량 >>> ')
        
        data2 = (name,int(sold))

        cursor.execute(sql,data2)

        cursor.close()
        conn.commit()
        conn.close()
                                   
    elif choice == 'L':
        while True:
            choice = input('''
다음 중에서 분류하실 종목을 골라주세요 :
1. product \t 2.stock \t 3.receive \t 4.sweet
>>> ''')
            if choice == '1':
                sql = "select * from fruit order by product asc"
                cursor.execute(sql)
                cursor.close()
                conn.commit()
                conn.close()
            
            elif choice == '2':
                sql = "select * from fruit order by stock asc"
                cursor.execute(sql)
                cursor.close()
                conn.commit()
                conn.close()

            elif choice == '3':
                sql = "select * from fruit order by receive asc"
                cursor.execute(sql)
                cursor.close()
                conn.commit()
                conn.close()

            elif choice == '4':
                sql = "select * from fruit order by sweet desc"
                cursor.execute(sql)
                cursor.close()
                conn.commit()
                conn.close()

            else:
                print('다시 선택해주세요')
                break

    elif choice == 'D':
        sql = "select product from fruit where stock = 0"
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()

    elif choice == 'Q':
        print('프로그램을 종료합니다')
        break

    else:
=======
import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()
# cursor.execute("create table fruit(product varchar2(100), stock number(3),price number(5),receive number(8),sweet number(1))")


while True:
    choice=input('''
다음 중에서 하실 일을 골라주세요 :
I - 입력 \t S - 판매 \t L- 재고 리스트 \t D-삭제 \t Q-종료
>>> ''').upper()
    if choice == 'I':
        sql = "insert into fruit values(:1,:2,:3,:4,:5)"
        cursor.execute("select * from fruit")
        product = input('과일명 >>>')
        stock = input('수량 >>> ')
        price = input('가격 >>> ')
        receive = input('입고일자 >>> ')
        sweet = input('당도 >>> ')
        data = (product,int(stock),int(price),int(receive),int(sweet))
        cursor.execute(sql,data)
        cursor.close()
        conn.commit()
        conn.close()

    elif choice == 'S':
        sql = "update fruit set stock = stock -sold where product = name"
        name = input('과일명 >>>')
        sold = input('수량 >>> ')
        
        data2 = (name,int(sold))

        cursor.execute(sql,data2)

        cursor.close()
        conn.commit()
        conn.close()
                                   
    elif choice == 'L':
        while True:
            choice = input('''
다음 중에서 분류하실 종목을 골라주세요 :
1. product \t 2.stock \t 3.receive \t 4.sweet
>>> ''')
            if choice == '1':
                sql = "select * from fruit order by product asc"
                cursor.execute(sql)
                cursor.close()
                conn.commit()
                conn.close()
            
            elif choice == '2':
                sql = "select * from fruit order by stock asc"
                cursor.execute(sql)
                cursor.close()
                conn.commit()
                conn.close()

            elif choice == '3':
                sql = "select * from fruit order by receive asc"
                cursor.execute(sql)
                cursor.close()
                conn.commit()
                conn.close()

            elif choice == '4':
                sql = "select * from fruit order by sweet desc"
                cursor.execute(sql)
                cursor.close()
                conn.commit()
                conn.close()

            else:
                print('다시 선택해주세요')
                break

    elif choice == 'D':
        sql = "select product from fruit where stock = 0"
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()

    elif choice == 'Q':
        print('프로그램을 종료합니다')
        break

    else:
>>>>>>> a08219a64da9ddeffedfcdc30de2ca7afe38677f
        print('다시 입력해주세요')