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

import os
directory = '.'

lst = os.walk(directory)
print(lst)