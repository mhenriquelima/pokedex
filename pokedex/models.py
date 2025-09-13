from django.db import models

# Create your models here.
class Pokemon(models.Model):
    pokedex_entry = models.IntegerField()
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    ability = models.CharField(max_length=100)
    type1 = models.CharField(max_length=100)
    type2 = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    stats = models.JSONField(blank=True, null=True)
    cry = models.CharField
    evolution_chart = models.CharField()
    location = models.CharField()
    ...
    
class Team(models.Model):
    poke1 = models.ForeignKey(Pokemon)
    item1 = models.CharField(max_length=100)
    poke2 = models.ForeignKey(Pokemon)
    item1 = models.CharField(max_length=100)
    poke3 = models.ForeignKey(Pokemon)
    item1 = models.CharField(max_length=100)
    poke4 = models.ForeignKey(Pokemon)
    item1 = models.CharField(max_length=100)
    poke5 = models.ForeignKey(Pokemon)
    item1 = models.CharField(max_length=100)
    poke6 = models.ForeignKey(Pokemon)
    item1 = models.CharField(max_length=100)