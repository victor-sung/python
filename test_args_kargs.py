def add(a, b, *args, **kargs):
    print(args) # position argument이다. tuple 형태(immutable 변경불가능)
    print(kargs)    # keyword argument이다.   dictionary 형태

    return a + b


add(1, 2, 3, 4, 5, test="test", boolean_false=False, boolean_true=True)
