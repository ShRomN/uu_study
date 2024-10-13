# def g(*b):
#     print(b)


# def f(*a):
#     print(a)
#     g(*list(a))



    
# f('a', b='b', c='c')


# from re import match, fullmatch

# s = 'university.help@gmail.com'

# print(fullmatch(r'^([a-zA-Z0-9_.-]+)\@([A-Za-z_-]+)\.((com)|(ru)|(net))$', s) is None)


# print('rich' in 'richiest')

# l = [1, 2, 3, 4, 5]
# l = range(1, 6)

# print(*l)

# lst = 'abcd'
# aaa = [lst.lower()]
# print(aaa)

# a = 10 
# b = (a, )
# print(b)

# print((10,  ) * 5)

# args = [1, 2, 3, 4, 5]
# print(all(map(lambda x: isinstance(x, int) and x > 0, args)))
# print(tuple(args))
# f(*args)
# f()

# import os
# directory = '.'

# lst = os.walk(directory)
# print(lst)

# f = min
# print(f.__name__)

# print(bool(-1))

# import re

# print(re.match(r'^\D+$', 'fg3k'))




# try:
#     a = 10
#     print(10 / 0)
# except Exception as e:
#     print(a + 1)
# else:
#     print(a)


if True:
    a = 10

if True:
    print(a)
