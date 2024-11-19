# Args and Kwargs

a, *b, c = {1: "one", 2: 'Two', 3: 'Three', 'f': 'Four', 'asd': 'alphobet'}.values()

print(a, b, c)


def foo(a, b, c, d, h):
    return (a, b, c, d, h)


a = ('hello', 23, True, 1.2, ['a', 'b', 'c'])
print(foo(*a))


def foo(**kwargs):
    for i, v in kwargs.items():
        print(i, v)
    print(kwargs)


foo(h='one', t='two', th='sdf', f='wer', )

a = map(str, [3, 4, 5, 6, 7, 8, 9])
print(*a)
