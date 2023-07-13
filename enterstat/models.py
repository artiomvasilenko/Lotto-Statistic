from django.db import models
from datetime import date
from django.urls import reverse

# Create your models here.

class Name(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название лотереи', blank=False, null=False)
    jackpot = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Lottery(models.Model):
    date = models.DateField(verbose_name='Дата розыгрыша', null=False, blank=False, default=date.today())
    name = models.ForeignKey(Name, on_delete=models.CASCADE, null=False, blank=False)
    price = models.IntegerField(verbose_name='Цена билета', null=False, blank=False)
    result = models.IntegerField(verbose_name='Сумма выигрыша', default=0)

    def __str__(self):
        str = f'{self.date} - {self.name}'
        return str

    class Meta:
        ordering = ['-date']