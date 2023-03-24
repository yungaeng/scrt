import re

bat_re = re.compile(r'Bat(wo)*man')
mo1 = bat_re.search('The Adventures of Batman')
mo1.group()
mo2 = bat_re.search('The Adventures of Batwoman')
mo2.group()
mo3 = bat_re.search('The Adventures of Batwowowowowowoman')
mo3.group()

""""
* 없거나 반복
+ 한번 또는 여러번
? 없거나 하나
{} 특정 횟수만큼 반복
{3,5} 3 or 4 or 5
[] or
[a-g] a부터 g까지
[^] -를 제외한 모든 것
^ 맨 앞 매칭 $ 맨 끝 매칭
.word word를 제외한 모즌 문자와 매칭
.*  모든 문자열에 매칭 
"""

phone_re = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
phone_re.findall('Cell: 415-555-9999 Work: 212-555-0000')

p = re.compile(r'^hello')
p.search('hello')
p.search('ahello')

p = re.compile('.at')
p.findall('The cat in the hat sat on the flat mat.')
p = re.compile(r'성:(.*)이름:(.*)')
p.search('성:이 이름:대현').groups()

p = re.compile(r'<.*?>')
p.search('<이대현> 님 입장하셨습니다. >').group()
#defult 값은 greedy, ? 를 붙이면 nongreedy

p = re.compile(r'hello', re.I)
p.search('Hello World')
p.search('HELLO WORLD')

text = '''this
is
multiple
line
'''

p = re.compile('.*', re.DOTALL)
p.search(text)

t = '제 1회 복권 담첨자는 <이대현> 입니다.'
p = re.compile('<(\D)\D{1,3}>')
p.search(t).group()

p.sub(r'\1**', t)
