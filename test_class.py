# self란 class의 인스턴스를 나타내는 변수이다. class내의 method들의 첫번째 인자로 전달된다.
# python은 이렇게 명시적으로 선언해 줘야 한다.
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(id(self))  # 객체의 메모리 주소를 출력
        print(__name__)
        print('hi~')

    def say_bye(self):
        print('bye~')


class Animal:
    age = 100


# man = Person()
# man.say_hello()
# print(id(man)) # man의 주소나 self의 주소는 동일하다. 즉 mac 인스턴스 = self이다.
#
# woman = Person()
# woman.say_hello()

person = Person('victor')
animal = Animal()

Person.say_hello(animal) # 첫 번째 인자인 self에 대한 값은 파이썬이 자동으로 넘겨주기 때문에 넘겨줄 필요가 없다.
print(id(person))
# print(dir(person))
print(person.__dict__)
print(globals())
print(__name__)