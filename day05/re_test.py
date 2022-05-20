import re

# a = 'hello, world!'
# print(re.match('world',a))
# print(re.search('world!$',a))

# str1 = '123 hello 678 HELLO'
# print(re.match('[0-9]+',str1))
# print(re.search('[0-9]*',str1))   ##앞에서부터 탐색

# print(re.match('a*b','aaaaab'))
# print(re.search('^[0-9]{2,3}-[0-9]{4}-[0.9]{4}$','002-1111-1111 tel'))

p = re.compile('^[a-z][a-z0-9_]{4,}@[a-z]{3,}[.][a-z]{2,}$')
email = ''

while not p.search(email):          #none이 나오면 반복되게
    email = input('email >>> ')
    break
    print(email)