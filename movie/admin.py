from django.contrib import admin
from movie.models import Movie, MovieRating


class MovieAdmin(admin.ModelAdmin):
    pass


admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieRating, MovieAdmin)
