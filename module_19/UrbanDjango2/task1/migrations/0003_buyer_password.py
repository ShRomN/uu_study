# Generated by Django 4.2.17 on 2025-01-16 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0002_alter_buyer_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='password',
            field=models.CharField(default=3, max_length=50, verbose_name='Пароль'),
            preserve_default=False,
        ),
    ]
