from django.db import models

# Create your models here.
class Pokemon(models.Model):
    pokemon_id = models.IntegerField()
    name = models.CharField(max_length=160, default=None)
    description = models.CharField(max_length=160, default=None)
    shape = models.CharField(max_length=160, default=None)
    main_color = models.CharField(max_length=160, default=None)
    egg_group = models.CharField(max_length=160, default=None)
    habitat = models.CharField(max_length=160, default=None)
    img = models.ImageField(null=True, blank=True)
    shiny_img = models.ImageField(null=True, blank=True)
    ears = models.BooleanField(default=False)
    legs = models.IntegerField()
    horns = models.BooleanField(default=False)
    tail = models.BooleanField(default=False)