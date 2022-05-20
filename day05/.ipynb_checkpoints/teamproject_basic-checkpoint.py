# 과일가게 재고 프로그램 구축

# 1. 기능
# 과일 입력(I), 과일 판매(S), 재고 리스트(L), 삭제(D)
#-괄호 안 영문자를 입력하면 각 기능이 구현되게 만든다
#json 이용

# 2. 입력(I) 
# -dictionary로 각 키의 값을 받고 빈 리스트에 채워나간다.
# -입고일자(receive):8자리로 입력해야함
#  ->Len 값으로 입력 값의 길이를 구함
#  ->8자리가 아닐 경우 재입력 하도록 함
# -당도(sweet):1~5사이의 값만 입력해야함
# -키 값 입력이 완료된 fruit 딕셔너리를 fruitlist에 추가(append)한다.
# - 상품명, 수량, 단가, 입고일자

# 3. 판매(S) 

# 4. 재고리스트(L)
# product, stock, receive, sweet 에 따라 정렬 가능하게 한다

# 5. 삭제(D)
# 수량이 0이 된 품목을 표시한다.

import json           

fruitlist=[]
fruitlist=[{'product': '사과', 'stock': 20, 'price': 1000, 'receive': 20220510, 'sweet':4}, {'product': '바나나', 'stock': 15, 'price': 500, 'receive': 20220508, 'sweet':2}, {'product': '토마토', 'stock': 25, 'price': 1500, 'receive': 20220506, 'sweet':3}]

# with open('fruitlist.json','r') as f:
#     fruitlist = json.load(f)


while True:
    choice=input('''
다음 중에서 하실 일을 골라주세요 :
I - 입력 \t S - 판매 \t L- 재고 리스트 \t D-삭제 \t Q-종료
>>> ''').upper()

    if choice == 'I':
        print(fruitlist)
        fruit = {'product':'','stock':'','price':'','receive':'','sweet':''}
        fruit['product'] = input('추가할 과일명을 입력하세요 >>>')

        while True: 
            fruit['stock'] = input('추가할 수량를 입력하세요 >>>')
            if fruit['stock'].isdecimal():
                fruit['stock'] = int(fruit['stock'])
                break

        while True:
            fruit['price'] = input('가격을 입력하세요 >>>')
            if fruit['price'].isdecimal():
                fruit['price'] = int(fruit['price'])
                break       

        while True:
            fruit['receive'] = input('입고일자 8자리를 입력하세요 >>> ')
            if len(fruit['receive']) == 8 and fruit['receive'].isdecimal():
                fruit['receive'] = int(fruit['receive'])
                break                                     

        while True:
            fruit['sweet'] = input('과일의 당도를 입력하세요 >>> ')
            if fruit['sweet'].isdecimal() and int(fruit['sweet']) in range(1,6): 
                fruit['sweet'] = int(fruit['sweet'])               
                break                              
            
        fruitlist.append(fruit)
        print(fruitlist)
        # with open('fruitlist.json','w') as f:
        #     json.dump(fruitlist,f)

    elif choice == 'S':
        while True:
            productlist = []
            for item in fruitlist:
                print(item['product'])
                productlist.append(item['product'])
        
            product = input('판매한 과일을 입력하세요 >>> ')
            if product == 'q':
                break

            elif product in productlist:
                idx = ''
                for i in range(len(fruitlist)):
                    if fruitlist[i]['product']==product:
                        idx = i
                        break
                
                count = input('판매한 수량을 입력하세요 >>> ')
                fruitlist[idx]['stock'] -= int(count)
                
                print(f"{count}개를 판매하여 {fruitlist[idx]['stock']}개가 남았습니다.")
                # with open('fruitlist.json','w') as f:
                #     json.dump(fruitlist,f)
                break
                                   
    elif choice == 'L':
        while True:
            choice = input('''
다음 중에서 분류하실 종목을 골라주세요 :
1. product \t 2.stock \t 3.receive \t 4.sweet
>>> ''')
            if choice == '1':
                data = sorted(fruitlist, key = lambda fruitlist: fruitlist['product'])
                for d in data:
                    print(d)
            
            elif choice == '2':
                data = sorted(fruitlist, key = lambda fruitlist: fruitlist['stock'])
                for d in data:
                    print(d)

            elif choice == '3':
                data = sorted(fruitlist, key = lambda fruitlist: fruitlist['receive'])
                for d in data:
                    print(d)

            elif choice == '4':
                data = sorted(fruitlist, key = lambda fruitlist: fruitlist['sweet'],reverse=True)
                for d in data:
                    print(d)

            else:
                print('다시 선택해주세요')
                break

    elif choice == 'D':
        for idx in range(len(fruitlist)):
            if fruitlist[idx]['stock'] == 0:
                print('품절: ',fruitlist[idx])
            else:
                print('재고가 있습니다')
                break
            
    elif choice == 'Q':
        print('프로그램을 종료합니다')
        # with open('fruitlist.json','w') as f:
        #     json.dump(fruitlist,f)
        break

    else:
        print('다시 입력해주세요')