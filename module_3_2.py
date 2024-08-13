from re import fullmatch

def send_email(message:str, recipient, *, sender:str="university.help@gmail.com"):
    """
    Функция отправки письма.
    """
    re_exp = r'^([a-zA-Z0-9_.-]+)\@([A-Za-z_-]+)\.((com)|(ru)|(net))$'
    
    # Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net".
    if fullmatch(re_exp, recipient) is None or fullmatch(re_exp, sender) is None:
        print(f'Невозможно отправить письмо с адреса {recipient} на адрес {sender}')
    
    # Если же sender и recipient совпадают
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')

    # Если отправитель по умолчанию - university.help@gmail.com
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')

    # В противном случае
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
