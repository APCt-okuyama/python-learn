
num = 1
name = 'mike'
is_ok = True

print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

num = name
print(num, type(num))

# 型変換
name = '123'
num = int(name)
print(num, type(num))

#型が宣言できる　あまり利用
num2:int = 100
print(num2)

###################################
print('Hi', 'Mike')
print('Hi', 'Mike', sep=',')
print('Hi', 'Mike', end='\n')
print('Hi', 'Mike', end='\n')

print(2+2)

# 数学関数
import math

result = math.sqrt(25)
print(result)

y = math.log2(10)
print(y)

print( math.sin(1) )
#print(help(math))

# 文字列
s = 'test'
print(s)

print("i don't know ")
print("i don\'t know ")
print('i don\'t know ')
print("i don\"t know ")

print('hello. \n how are u?')
print('C:\name\name')
# row
print(r'C:\name\name')
# 複数行
print("##################")
print("""\
aaa
bbb
ccc\
""")
print("##################")

print('Hi. ' * 3 + 'Mike. ')

print('Py' + 'thon')
prefix = 'Py'
print(prefix + 'thon')


s = (
    'aaaaaaaaaaaaaaaa'
    'bbbbbbbbbbbbbbbb'
    )
print(s)

word = 'python'
print(word)
print(word[0])
print(word[1])
print(word[-1])
print(word[-2])
print(word[0:5])
print(word[:2])
print(word[2:])

#print(word[20])

print('########################')

word = 'j' + word[1:]
print(word[:])

n = len(word)
print(n)


s = 'my name is mike.'
print(s)
is_start = s.startswith('my')
print(is_start)

print("###########################")

print(s.find('mike'))
#print(s.replace('m','a'))

# 文字のフォーマット
print( 'my name is {0} {1}'.format('a', 'b') )


# リスト
l = [1,2,3,4]
print(l)
print(l[1])

print(l[0:2])

print(len(l))

# n = l[20]

print(l[::2])


s = ['a','b','c','d','e','f','g']
print(s)
print(s[0])
print(s[2:4])
s[2:4] = []
print(s)
s[2:4] = ['X','Y']
print(s[:])

n = [1,2,3,4,5,6,7,8,9]
print(n)

n.append(100)
print(n)

n.insert(0, 200)
print(n)

n.pop()
print(n)

n.pop(0)
print(n)

del n[0]
print(n)

n.remove(2)
print(n)

del n

a = [1,2,3]
b = [4,5,6]
x = a + b
print(x)

a += b
print(a)

a.extend(b)
print(a)

print('#####################')

r = [1,2,3,4,5,1,2,3]
print(r.index(3))
print(r.index(3,3))

print(r.count(3))
if 5 in r:
    print('5 is there...')

r.sort()
print(r)

r.sort(reverse=True)
print(r)

r.reverse()
print(r)

s = 'my name is Mike'
to_sprit = s.split(' ')
print(to_sprit)

# リストのコピー

i = [1,2,3,4,5]
j = i
print(i)
print(j)

# 参照渡し
j[0] = 100
print(i)
print(j)

# 
x = [2,2,2,2,2]
y = x.copy()
#y = x[:] copyと同じ
print(x)
print(y)
y[0] = 100
print(x)
print(y)

z = x
print(id(x))
print(id(y))
print(id(z))

##############

seat = []
min = 0
max = 5

print( min <= len(seat) < max )
seat.append(1)
seat.append(1)
seat.append(1)
seat.append(1)
seat.append(1)
print( min <= len(seat) < max )
seat.pop()
print( min <= len(seat) < max )


# タプル型
# t = [] これはリスト
t = (1,2,3,4,5)
print(t, type(t))

print(t[3])

print(t.index(3))
print(t.count(2))
# タプルにリストを入れる
t = ([1,1,1,1],[2,2,2,2])
print(t)
t[1][1] = 100
print(t)

t = 3, 3, 3
print(t, type(t))

# これはtaple
t = 3, 
print(t, type(t))

# これはint
t = 3
print(t, type(t))

# これはint
t = (3)
print(t, type(t))


# tupleは変更不可だけど
new_tuple = (1,2,3) + (4,5,6)
print(new_tuple)

#tupleのアンパック
num_tuple = (11,22)
x, y = num_tuple
print(x,y)

x, y = 3, 4
print(x,y)

# tupleのアンパッキングをつかった入替
i = 10
j = 20
print(i,j)
i,j = j,i
print(i,j)

# tupleの使い道

chose_from_two = ('A','B','C')
answer = []
answer.append('A')
answer.append('B')

print(chose_from_two)
print(answer)


# disc
d = { 'x': 10, 'y':20 }
print(d)
print(d['x'])
d['x'] = 'test'
print(d['x'])

d['z'] = 'zzz'
d['1'] = 1000
print(d)

d2 = dict(a=10, b=100, c=1000)
print(d2)

d3 = dict([('a', 1), ('b', 2)])
print(d3)

#辞書メソッド
d = {'x':10, 'y':20}
print(d)

print(d.keys())
print(d.values())

d2 = {'x':101, 'y':201, 'a': "aaa"}
print(d2)

d.update(d2)
print(d)

d.pop('a')
print(d)

print( 'a' in d )
print( 'x' in d )


# dict copy
x = {'a':1}
#y = x
y = x.copy()
y['a'] = 3
print(x)
print(y)

fruits = {
    'apple':100,
    #'apple':200,    
    'banana': 200,
    'orange' : 300
}

print(fruits)
print(fruits['apple'])

# dictionary は　ハッシュテーブル

# 集合
a = {1,2,3,4,5,5,6}
b = {1,3,7}
print(a, type(a)) # typeはset

print("####### 集合(set) ##########")
print( a - b )
print( b - a )
print( a & b )
print( a | b )

print("#################")
s = {1,2,3,4,5}
print(s, type(s))
s.add(6)
print(s, type(s))
s.add(6)
print(s, type(s))
s.remove(6)
print(s, type(s))
s.clear()
print(s, type(s))

# 集合の使いみち 共通
my_friends = {'A','B','C'}
a_friends = {'B','D'}
print(my_friends & a_friends)

# list => dict 重複を取り除く
f = [1,2,3,4,1,2,4]
kind = set(f)
print(kind)

# コメント
"""
これは複数行のコメント
これは複数行のコメント
これは複数行のコメント
"""
print("test")


# 制御フロー
s = 'aaaa' \
    + 'bbbb'
print(s)

x = 1 + 1 + 1 + \
    1 + 1 + 1
print(x)

y = ( 1 + 1 + 1 + 
    1 + 1 + 1 )
print(y) 

# if
x = 0
if x < 0:
    print('negative.')
elif x == 0:
    print('zero')
else:
    print('positive.')

# in と not
x = [1,2,3,4,5]
y = 1

if y in x:
    print('in')
if 10 not in x:
    print('not in')

if 0:
    print('zero')
if 1:
    print('one')

#is_ok = 'a'
#is_ok = [1,2,3,4]
is_ok = []
if is_ok:
    print('true')
else:
    print('false')

# null的な変数
is_empty = None
print(is_empty, type(is_empty))

# is は None を判定するときに利用
if is_empty is None:
    print('This is None')

# loop
count = 0
while count < 5:
    print(count)
    count += 1

count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        print('break')
        break
else: # 最後に実行 ※breakで抜けると実行されない
    print('done')
1
# input関数
# while True:
#     word = input('Enter:')
#     num = int(word)
#     #if word == 'ok':
#     if num == 100:
#         break
#     print('next')

# for
some_list = [1,2,3,4,5]
# i = 0
# while i < len(some_list):
#     print(some_list[i])
#     i += 1
for i in some_list:
    print(i)

for s in 'abcde':
    print(s)

for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        continue
        #break
    print(word)

for fruit in ['apple','orange','banana']:
    # if fruit == 'orange':
    #     break
    print(fruit)
else:
    print('i ate all.')

# range関数
num_list = [1,2,3,4,5]
for i in num_list:
    print(i)

print('###')
for i in range(2, 10, 3):
    print(i)

print('###')
# _ は利用しないことの明示
for _ in range(10):
    print('hello')

print('###')
# enumerate関数 
for i, fruit in enumerate(['apple','orange','banana']):
    print(i, fruit)

# zip関数 まとめてループ
days = ['Mon','Thu','Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']
for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

# dictionaryのループ
d = { 'x':100, 'y':200 }
print(d)
print(d.items())
for k, v in d.items():
    print(k, v)

# 関数定義
def say_something():
    print('hi something...')

print(type(say_something))
say_something()

f = say_something
f()

def say_something2():
    s = 'hi something2'
    return s
print(say_something2())


def what_is_this(color):
    print(color)
what_is_this('red')


# 関数の型 
def add_num(a: int, b: int) -> int:
    return a + b
print( add_num(1,2) )
# 型の宣言ではエラーにならない
print( add_num('1','2') )

def menu(entree, drink, dessert):
    print(entree, drink, dessert)

menu('test', 'test1', 'test2')
# キーワード引数
menu(entree='test', dessert='test2', drink='test1' )
menu('test', dessert='test2', drink='test1' )

#デフォルト引数
def menu2(entree='a', drink='b', dessert='c'):
    print(entree, drink, dessert)
menu2(entree='dddd')

def test_func(x, l=[]):
    l.append(x)
    return l

y=[1,2,3]
r = test_func(10,y)
print(r)
print(y)

# デフォルト引数の配列が同じ配列となる
r = test_func(100)
print(r)
r = test_func(100)
print(r)


# 空のリストやDictの場合に注意
def test_func2(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l
print(test_func2(10))
print(test_func2(10))


# 複数の引数
def say_something(word, *args):
    print(word)    
    print(args) # tuple
say_something('a','b','c', 'd', 'e')
t = ('Mike', 'Nancy')
say_something('a', *t)

# キーワード引数の辞書化
def menu(**kwarges):
    print(kwarges)
    # 辞書として扱える
    for k, v in kwarges.items():
        print(k,v)

menu(entree='aaa', drink='bbbb')

d = {
    'aaa':'aaa',
    'bbb':'bbb',
    'ccc':'ccc'    
}

# 辞書として渡す、展開されて渡される
menu(**d)

def menu2(food, *args, **kwargs):
    print(food)
    print(args) # tuple
    print(kwargs) # 辞書

menu2('aaa', 'bbb', 'ccc', ddd='ddd', eee='eee')

# Docstrings
def test_func(param1, param2):
    """ functionsの説明をここに書く
    Args:
        param1
    Returns:
        bool:
    """
    print(param1)
    print(param2)
    return True

print(test_func.__doc__)
#help(test_func)

# 関数内関数 (inner func)
def outer(a,b):
    print(a,b)

    #インナー関数として定義できる
    def plus(c,d):
        return c+d
    
    r = plus(a,b)
    print(r)

outer(2,3)


# クロージャー
def outer(a,b):
    def inner():
        return a + b
    return inner # 関数を返す
print(outer(1,2))
f = outer(1,2) # 関数を戻り値として受け取る
r = f() # 関数を実行
print(r)

def circle_area_func(pi):
    def circle_area(r):
        return pi * r * r
    return circle_area

cal1 = circle_area_func(3.14)
cal2 = circle_area_func(3.141592)

print(cal1(10))
print(cal2(10))

# デコレーター 関数をラップして共通処理を纏める
def print_info(func): #デコレーター関数
    def wrapper(*args, **kwargs):
        print('start')
        print('func_name:', func.__name__)
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper # 関数を返す

@print_info
def add_num(a, b):
    return a + b

f = print_info(add_num)
r = f(10, 20)
print(r)

# @でデコレーターを指定できる
# 他の関数にも適用できる
# 複数指定することもできる（順序に注意）
@print_info
def add_num2(a, b):
    return a + b

r = add_num2(5, 5)
print(r)

# ラムダ
l = ['Mon', 'tue', 'Wed', 'Thu', 'Fri']

def change_words(words, func):
    print(func.__name__)
    for word in words:
        print(func(word))

def sample_func(word):
    return word.capitalize()

sample_func2 = lambda word: word.capitalize()

change_words(l, sample_func)
change_words(l, sample_func2)
change_words(l, lambda word: word.capitalize())

# ジェネレーター yield と next の利用方法
print('ジェネレーター')
l = ['aaa','bbb','ccc']

for i in l:
    print(i)

def test():
    yield 'ddd'
    yield 'eee'
    yield 'fff'
for t in test():
    print(t)

t = test()

def counter(num=10):
    for _ in range(num):
        yield 'run'

c = counter()


print(next(t))
print('@@@')
print(next(c))
print(next(c))
print(next(c))
print(next(t))
print('@@@')
print(next(c))
print(next(c))
print(next(c))
print(next(t))
#print(next(t)) #stopiteration これはエラーになる。


# リスト内包表記
t = (1,2,3,4,5)
r = [ i for i in t]
print(r)

r2 = [ i for i in t if i % 2 == 0]
print(r2)

t2 = (5,6,7,8,9)

r3 = []
for i in t:
    for j in t2:
        print(i*j)
        r3.append(i * j)
print(r3)

r4 = [i * j for i in t for j in t2]
# あまりforを繰り返すと可読性が下がるので注意
print(r4)

# 集合(set)内包表記
s = set()

for i in range(10):
    s.add(i)
print(s)

s = { i for i in range(10) if i % 2 == 0}
print(s)

# ジェネレーター内包表記
def g():
    for i in range(10):
        yield i

g = g()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

g2 = (i for i in range(10)) # これの type は generator になる
print(type(g2)) 
print(next(g2))
print(next(g2))
print(next(g2))


# 名前空間とスコープ
animal = 'cat'
print(animal)

def f():
    global animal    
    print('global', animal)
    # ローカル変数があると上のanimalがローカル変数を参照することになる
    # animal = 'dog' 
    # global

    animal = 'dog'    
    print('local', animal)

    print('locals():', locals())
    #print('locals():', globals())    

    print(__name__)
f()

print(__name__)

# 例外処理
l = [1,2,3]
i = 2

#del l

try:
    l[i]
except IndexError as ex:
    print('index err {}'.format(ex))    
except NameError as ex:
    print('name error dont worrry')
except Exception as ex: # すべてキャッチする
    print('other error')
else:
    print('else done これは成功した場合のみ実行される')
finally:
    print('run finally errorでも必ず実行されます')
print("end.")


# 独自の例外処理
class MyUppercaseError(Exception):
    pass

def check():
    words = ['aaa', 'bbb']
    raise MyUppercaseError('my message')

try:
    check()
except MyUppercaseError as ex:
    #独自の例外とわかるようにしましょう（分かりやすくなる）
    print('this is my uppercase error')

