from django.urls import path

from . import views

urlpatterns = [
    path('', views.MovieView.as_view()),
    path('<int:slug>/', views.MovieDetailView.as_view(), name="movie_detail")
]