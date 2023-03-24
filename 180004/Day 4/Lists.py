black_pink = ['jisu', 'jeni', 'lisa', 'rose']
black_pink[1:3]
num = '0123456789ABCDEF'
num[::-1]
spam = [['cat', 'bat'], [1,2,3,4,5]]
type(spam)
spam[1][0]
len(black_pink)
black_pink[0] = 'daehyun'
black_pink.append('JYP')
black_pink += ['YG']
black_pink.remove('JYP')
del black_pink[0]
black_pink.insert(2, 'IU')

for member in black_pink:
    print(member)

for i in range(len(black_pink)):
    print(i, black_pink[i])

# enumerate 사용
for i, member in enumerate(black_pink):
    print(i, member)

# 멤버가 있는지 판결
'YG' not in black_pink

black_pink.index('YG')

spam = [2, 5, 3, 1, -7]
spam.sort(reverse=True)
spam

data = ['A', 'B', 'C', 'D']
new_data = data
new_data is data
id(new_data) == id(data)

new_data[0] = 'X'
data

new_data = data.copy()
new_data == data
new_data is data

new_data[0] = 'F'
data

values = [i for i in range(10)]
values
odd_values = [n for n in range(20) if n % 2 == 1]
odd_values
[(x,y) for x in [1,2,3] for y in ['a', 'b', 'c']]
vac = [[1,2,3],[4,5,6],[7,8,9]]
# 다중배열이 있을 경우 평평하게 만들다 flat
[num for elem in vac for num in elem]
import random
values = [random.randint(0, 5) for i in range(20)]
values
[v if v != 0 else 'ZERO' for v in values]
# 튜플 값은 변경 불가능 READ만 가능

t2 = (100,)
type(t2)
# 원소가 하나인 튜플 구분
t3 =(100)
type(t3)
t4 = ()
type(t4)
t5 = (2,3,4,5)
t6 = (6,7,8)
t5 + t6


def add(*values):
    result = 0
    for v in values:
        result += v
    return result


def newadd(*values):
    return sum(values)

newadd(1,2,3,4,5,6)

add(1,2,3)