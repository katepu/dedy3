from django.db import models

# !!! мы только описываем тут таблицы(структуру), а миграции уже записывают в БД через команды в терминале:
# > python3 manage.py makemigrations > python3 manage.py migrate > python3 manage.py runserver?
# ТАК ДЕЛАТЬ КАЖДЫЙ РАЗ КОГДА МЕНЯЕТСЯ СТРУКТУРА БД !!!


# это как одна таблица в БД
class Worker(models.Model):
    name = models.CharField(max_length=15, blank=False)
    surname = models.CharField(max_length=15, blank=False)
    age = models.IntegerField()
    salary = models.IntegerField(default=0)
    position = models.CharField(max_length=50)
    # после добавления методов НЕ нужно делать миграции !!!
    def __str__(self):
        return self.name # или self.surname - это будет отображаться в админке
        # return f'{self.name} {self.surname}'  можно и так

#это как другая таблица в БД
class Equipment(models.Model):
    name = models.CharField(max_length=15, blank=False)
    price = models.IntegerField()
    purchase_date = models.DateField()
    # после добавления методов НЕ нужно делать миграции !!!
    def __str__(self):
        return self.name