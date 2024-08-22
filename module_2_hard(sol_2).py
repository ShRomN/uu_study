from random import randint

n = randint(3, 20)
# n = 10
print(n)
print(''.join(list(map(lambda el: ''.join(el), ([f'{j}{z}' for z in range(j + 1, n) if n % (j + z) == 0] for j in [i for i in range(1, n)])))))
