example = 'Тестовая строка'
print(example[0])
print(example[-1])
print(example[((len(example) + 1) // 2) - (len(example) % 2) - (1 - ((len(example) - len(example) // 2)) % 2):])
print(example[::-1])
print(example[1::2])
