from django.db import models
from musician.models import Musician

class Album(models.Model):
    name = models.CharField(max_length=50)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField()
    # rating = models.CharField(max_length=1, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])

    def __str__(self):
        return self.name