from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms

# listings/models.py

class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH', 'Hip-Hop'
        SYNTH_POP = 'SP', 'Synth-Pop'
        ALTERNATIVE_ROCK = 'AR', 'Alternative Rock'

    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=5, choices=Genre.choices)
    biography = models.CharField(max_length=1000)
    year_formed = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    active = models.BooleanField(default=True)
    official_homepage = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Listing(models.Model):
    title = models.CharField(max_length=100)

    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
    
