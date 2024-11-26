def single_root_words(root_word, *other_words):
    """
    Функция фильтрации списка строк по наличию одинаковых полстрок.
    """
    # same_words = []
    # for word in other_words:
    #     if root_word.lower() in word.lower() or word.lower() in root_word.lower():
    #         same_words.append(word)
    
    # return same_words
    return list(filter(lambda x: root_word.lower() in x.lower() or x.lower() in root_word.lower(), other_words))


# Тестовые данные
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
