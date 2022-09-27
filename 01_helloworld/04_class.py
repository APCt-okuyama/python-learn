# class

from dataclasses import make_dataclass
from pyexpat import model


s = 'asdfkjelfkjs'
print(s.capitalize())

##
class Person(object):
    def say_something(self):
        print('hello')
    def say_anything(self):
        print('aaa')

p = Person()
p.say_something()
p.say_anything()

class Person2(object): 
    def __init__(self, name) -> None:
        self.name = name
        print('first これはコンストラクタ')
    def func(self):
        print('hello. {}'.format(self.name))
        self.run()
    def run(self):
        print('run start')
    def __del__(self):
        print('__del__ これはデストラクタ')
p2 = Person2('Mike')
p2.func()
del p2
print('#########')

# クラスの継承
class Car(object):
    def __init__(self, model=None) -> None:
        self.model = model
    def run(self):
        print('car:run')

class ToyotaCar(Car):
    # pass
    def run(self): # メソッドオーバーライド
        print('toyotacar:run')

class TeslaCar(Car):
    def __init__(self, model=None, enable_auto_run=False, password='1234') -> None:
        # 親クラスの初期化処理
        super().__init__(model)
        #プロパティ _
        self._enable_auto_run = enable_auto_run
        self._enable_auto_run2 = enable_auto_run
        self.__enable_auto_run3 = enable_auto_run        
    #プロパティの定義　getter
    @property
    def enable_auto_run(self):
        return self._enable_auto_run
    #プロパティの定義　setter
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        self._enable_auto_run = is_enable    
    # pass
    def auto_run(self):
        print('Teslacar:auto run : ', self.model) 
        print(self.__enable_auto_run3)   

teslacar = TeslaCar('Tesla')
teslacar.run()
teslacar.auto_run()

teslacar.enable_auto_run = True
print( teslacar.enable_auto_run )

teslacar.__enable_auto_run2 = True
print(teslacar._enable_auto_run2)

#print(teslacar.__enable_auto_run3)

# クラス構造体
class T(object):
    pass
t = T()
t.name = 'aaaa'
t.age = 30
print(t)

# ダッグタイピング
# 抽象クラス javaのインターフェースと同じ　あまり多様しない方が良いらしい
import abc
class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=123) -> None:
        self.age = age

    @abc.abstractmethod
    def drive(self):
        pass

class Adult(Person):
    def drive(self):
        print('実装する必要がある')

a = Adult()

# 多重継承
class Person2(object):
    kind = 'human' # クラス変数　すべてのオブジェクト間で共有の領域

    def talk(self):
        print('talk')

    @staticmethod
    def about(year):
        print('about human {}'.format(year))

class Car2(object):
    def run(self):
        print('run')
class PersonCar(Person2, Car2):

    def fly(self):
        print('fly 多重継承のサンプル')

person2 = PersonCar()
person2.talk()
person2.run()
person2.fly()

# 静的メソッド
person2.about(123)
PersonCar.about(234)

# 特殊メソッド
class Word(object):
    def __init__(self, text) -> None:
        self.text = text
    def __str__(self) -> str:
        return 'word test'
    def __len__(self):
        return len(self.text)
    def __add__(self, word):
        return self.text.lower() + word.text.lower()
w = Word('aa')
w2 = Word('bb')

print(w)
print(w2)
print(w + w2)
