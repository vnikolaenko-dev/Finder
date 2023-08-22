from django.db import models

"""
Модели для базы данных
"""


class Project(models.Model):
    # Столбцы
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    image = models.ImageField(upload_to='images')

    # Вывод
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class User(models.Model):
    # Столбцы
    name = models.CharField('Имя', max_length=20)
    email = models.CharField('Почта', max_length=50, unique=True)
    password = models.CharField('Пароль', max_length=20)
    image = models.ImageField(upload_to='images')

    # Вывод
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Text(models.Model):
    # Столбцы
    email = models.CharField('Почта', max_length=50, blank=True)
    text = models.TextField('Запись')
    sent = models.DateField('Время', blank=True)

    # Вывод
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
