def menu_input(menu):              #분리시 (값)
    print('현재메뉴 :',list(menu.keys()))
    name = input('추가할 메뉴명을 입력하세요>>>')
    price = 'a'
    while not price.isdecimal():
        price = input('추가할 메뉴의 가격을 입력하세요>>>')
    menu[name]=int(price)

def menu_update(menu):
    print('현재메뉴 :',list(menu.keys()))
    name = ''
    while not name in menu.keys():
        name = input('수정할 메뉴명을 입력하세요>>>')
    price = 'a'
    while not price.isdecimal():
        price = input('수정할 메뉴의 가격을 입력하세요>>>')
    menu[name]=int(price)

def menu_list(menu):
    print('------ menu ------')
    for item in sorted(menu.items(),key=lambda x:x[1],reverse=True):
        print(f'{item[0]} : {item[1]:,}')

def menu_delete(menu):
    print('현재메뉴 :',list(menu.keys()))
    name = ''
    while not name in menu.keys():
        name = input('삭제할 메뉴명을 입력하세요 >>>')
    del menu[name]