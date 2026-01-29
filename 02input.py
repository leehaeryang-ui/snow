#02input.py
a,b,total = 0,0,0

total =a+b
print(a,'+',b,'=',total)
print('{} + {} = {}'.format(a,b,total))
print(f'{a} + {b} = {total}')

a = input('첫번째숫자 a 입력하세요')
b = input('두번째숫자 b 입력하세요')

total = int(a) + int(b)
print(a,'+',b,'=',total)
print('{} + {} = {}'.format(a,b,total))
print(f'{a} + {b} = {total}')

#예외처리 try~except