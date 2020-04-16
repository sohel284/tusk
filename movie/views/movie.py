from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from movie.models import Movie
from movie.serializers import MovieSerializer


class MovieListCreateAPIView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class MovieRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = MovieSerializer
    queryset = Movie.objects.filter()
    lookup_field = 'id'


