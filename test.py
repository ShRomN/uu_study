
def f(a, *, b, c):
    print(a, b, c)
    
f('a', b='b', c='c')


from re import match, fullmatch

s = 'university.help@gmail.com'

print(fullmatch(r'^([a-zA-Z0-9_.-]+)\@([A-Za-z_-]+)\.((com)|(ru)|(net))$', s) is None)


print('rich' in 'richiest')