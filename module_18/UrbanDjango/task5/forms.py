from django.forms import Form, CharField, IntegerField

class UserRegister(Form):
    username = CharField(max_length=30, label='Введите логин')
    password = CharField(min_length=8, label='Введите пароль')
    repeat_password = CharField(min_length=8, label='Повторите пароль')
    age = CharField(max_length=3, label='Введите свой возраст')
