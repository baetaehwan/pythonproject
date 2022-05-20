stock = {}
i = 1
while i != 4:
    i = int(input("메뉴 \n1. 입고 \t 2. 출고 \n3. 현황확인 \t 4. 종료 \n 메뉴를 선택하세요 >>> "))
    if i == 1:
        a = input("입고 상품명 : ")
        b = int(input("해당 상품수 : "))
        if a in 재고.keys():
            재고[a] += b
        else:
            재고[a] = b
        print("입고처리됐습니다.")
    elif i ==2:
        a = input("출고 상품명 : ")
        b = int(input("출고 상품수 : "))
        if a in 재고:
            if 재고[a] >= b:
                재고[a] -= b
                print("상품이 {} 개 출고되었습니다.".format(b))
            elif 재고[a] < b:
                print("재고가 부족합니다.")
        else:
            print("해당 상품은 존재하지 않습니다.")
            print("현재 재고 현황은 아래와 같습니다")
            for k,v in 재고.items():
                print(k,":",v)
    elif i ==3:
        print("현재 재고 현황은 아래와 같습니다")
        for k,v in 재고.items():
            print(k,":",v)
    elif i==4:
        print("종료하겠습니다")
    else:
        print("잘못된 입력입니다.")