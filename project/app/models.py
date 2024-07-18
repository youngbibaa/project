from platform import release
from django.db import models

class Actor(models.Model):
    GENDER = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=240)
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    actors = models.ManyToManyField(Actor, related_name="movies")

    def __str__(self):
        return self.title
