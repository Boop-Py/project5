from django.db import models

# Create your models here.
class Pokemon(models.Model):
    pokemon_id = models.IntegerField()
    name = models.CharField(max_length=160, default=None)
    description = models.CharField(max_length=160, default=None)
    shape = models.CharField(max_length=160, default=None)
    main_color = models.CharField(max_length=160, default=None)
    egg_group = models.CharField(max_length=160, default=None)
    secondary_egg_group = models.CharField(max_length=160, default=None)
    habitat = models.CharField(max_length=160, default=None)
    img = models.ImageField(null=True, blank=True)
    shiny_img = models.ImageField(null=True, blank=True)
    evolves_from = models.CharField(max_length=160, default=None)
    main_type = models.CharField(max_length=160, default=None)
    secondary_type = models.CharField(max_length=160, default=None)
    ears = models.BooleanField(default=False)
    more_than_two_legs = models.BooleanField(default=False)
    horns = models.BooleanField(default=False)
    tail = models.BooleanField(default=False)
    fins = models.BooleanField(default=False)
    beak = models.BooleanField(default=False)
    wings = models.BooleanField(default=False)
