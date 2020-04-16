from django.db import models
from movie.models import Movie


class MovieRating(models.Model):
    movie = models.ForeignKey('movie.Movie', on_delete=models.CASCADE, )
    count = models.IntegerField()
    values = models.DecimalField(max_digits=2, decimal_places=1, )

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'rating'
