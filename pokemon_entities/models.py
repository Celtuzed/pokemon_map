from unittest.mock import DEFAULT
from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    title = models.CharField(verbose_name="Имя на русском", max_length=200)
    title_jp = models.CharField(verbose_name="Имя на японском", max_length=200, blank=True)
    title_en = models.CharField(verbose_name="Имя на английском", max_length=200, blank=True)
    image = models.ImageField(verbose_name="Картинка", blank=True)
    description = models.TextField(verbose_name="Описание", blank=True)
    previous_evolution = models.ForeignKey('self', verbose_name="Предыдущая эволюция", on_delete=models.SET_NULL, related_name='next_evolutions', null=True, blank=True)

    def __str__(self):
        return self.title

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name="Покемон", related_name='entities', on_delete=models.CASCADE)
    lat = models.FloatField(verbose_name="Широта")
    lon = models.FloatField(verbose_name="Долгота")
    appeared_at = models.DateTimeField(verbose_name="Добавлен в", null=True, blank=True)
    disappeared_at = models.DateTimeField(verbose_name="Удалён в", null=True, blank=True)
    level = models.IntegerField(verbose_name="Уровень", null=True, blank=True)
    health = models.IntegerField(verbose_name="Здоровье", null=True, blank=True)
    sterngth = models.IntegerField(verbose_name="Сила", null=True, blank=True)
    defence = models.IntegerField(verbose_name="Защита", null=True, blank=True)
    stamina = models.IntegerField(verbose_name="Выносливость", null=True, blank=True)
