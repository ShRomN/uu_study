def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    
    for i, s in enumerate(strings):
       strings_positions[(i + 1, file.tell())] = s
       file.write(s + '\n')

    return strings_positions


# Тестовые данные
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
