from django.db import models


class Buyer(models.Model):
    """
    Класс модели содержащий информацию о покупателе.
    """
    name = models.CharField(verbose_name='Имя покупателя', max_length=50)
    password = models.CharField(verbose_name='Пароль', max_length=50)
    balance = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Баланс счета покупателя')
    age = models.PositiveIntegerField(verbose_name='Возраст покупателя')

    def __str__(self) -> str:
        return self.name


class Game(models.Model):
    """
    Класс модели содержащий информацию о игре.
    """
    title = models.CharField(verbose_name='Название игры', max_length=100)
    cost = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Цена игры')
    size = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Размер файлов игры')
    description = models.TextField(verbose_name='Описание игры')
    age_limited = models.BooleanField(verbose_name='Ограничение возраста для игры', default=False)
    buyer = models.ManyToManyField(Buyer, related_name='byers')

    def __str__(self) -> str:
        return self.title
