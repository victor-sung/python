def my_sum1(a, b, c):
    print(a + b + c)


my_list = [1, 2, 3]
my_sum1(*my_list)


def my_sum2(*tests):
    result = 0
    for x in tests:
        result += x
    return result


list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]

print(my_sum2(*list1, *list2, *list3))

a = [*"RealPython"]
print(a)

*b, = "RealPython"
print(b)


def concatenate_values(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result


print(concatenate_values(a="Real", b="Python", c="Is", d="Great", e="!"))


def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs:
        result += arg
    return result


print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
