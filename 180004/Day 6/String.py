print(r'That is Carol\'s cat')


def print_line():
    print('''   
애국가:
    동해물과
    백두산이
애국가 끝
    
    ''')


print_line()

""""
여기는
주
석
입
니다
"""

data = 'spam'
data.upper()
data.startswith('s')
data.endswith('M')
data.startswith('sp')

'my name is hyun'.split() # 모든 공백 space, \n \t \v \f \r
'my name is hyun\ni love you'.split()
'my name is hyun\ti love you'.split()
'my name is hyun'.split()
'my name is      hyun'.split(' ')
'my name is hyun'.split('m')
'my namme is hyun'.split('m')
'my name is hyun'.split('is')
'my name isis hyun'.split('is')


import pyperclip

pyperclip.copy('hello world')