from django.urls import path
from cinema.views import *
app_name = "cinema"

urlpatterns = [
    path("movies/", movies,
         name="movie_list"),
    path("movies/<pk>/", movie_detail,
         name="movie_detail"),
]
