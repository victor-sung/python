def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def greet_bob(def_func):
    return def_func("Bob")

# 파이썬에서 함수는 일급 객체 입니다. 이는 다른 객체(string, int, float, list 등)와 마찬가지로 함수를 전달하고 인수로 사용할 수 있음을 의미합니다 .
print(greet_bob(say_hello))
print(greet_bob(be_awesome))
