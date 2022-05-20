def personal_info(name,age,address):
    print('name',name)
    print('age',age)
    print('address',address)

personal_info('홍길동',22,'대구')
personal_info(**{'name': '홍','address':'부산','age':33})


def personal_info1(**info):            ###몇개가 들어오는지 몰라서 *(튜플-같은종류의 값) **(딕셔너리)
    # print(info)
     for k,v in info.items():
        print(k,v)                     #밑에두줄 잠구면 딕셔너리형식

personal_info1(name='홍',address='부산',age=33,tel='111-2222')
