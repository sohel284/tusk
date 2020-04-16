from django.urls import path
from movie.views import MovieListCreateAPIView, MovieRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', MovieListCreateAPIView.as_view(), name='movie is crested'),
    path('<int:id>/', MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie delete and update')
]


