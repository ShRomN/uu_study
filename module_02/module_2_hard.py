from random import randint

n = randint(3, 20)
print(n)
lst = []

for i in range(1, n):
    for j in range(i + 1, n):
        if n % (i + j) == 0:
            lst.append([i, j])

print(lst)
result = ''.join(map(lambda pair: str(pair[0]) + str(pair[1]), lst))
print(result)
