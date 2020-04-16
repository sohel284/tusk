from django.db import models
from django.utils.translation import ugettext_lazy as _


class Movie(models.Model):
    MOVIE_GENRE = {
        ('DRAMA', _('drama', ),),
        ('ROMANTIC', _('romantic', ),),
        ('HISTORY', _('history', ),),
        ('ACTION', _('action', ),),
        ('BIOGRAPHY', _('biography', ),),
        ('FICTION', _('fiction', ), ),
    }
    title = models.CharField(max_length=50, )
    image = models.TextField(null=True, blank=True, )
    genre = models.CharField(max_length=50, )
    overview = models.TextField(max_length=50, )
    uploaded_time = models.DateTimeField(auto_now=True, )


    def __str__(self):
        return self.title
