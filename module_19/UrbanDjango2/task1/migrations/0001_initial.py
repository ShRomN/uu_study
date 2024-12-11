# Generated by Django 4.2.17 on 2024-12-11 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя покупателя')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Баланс счета покупателя')),
                ('age', models.IntegerField(verbose_name='Возраст покупателя')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название игры')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена игры')),
                ('size', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Размер файлов игры')),
                ('description', models.TextField(verbose_name='Описание игры')),
                ('age_limited', models.BooleanField(default=False, verbose_name='Ограничение возраста для игры')),
                ('buyer', models.ManyToManyField(related_name='byers', to='task1.buyer')),
            ],
        ),
    ]