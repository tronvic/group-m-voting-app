from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("candidates", views.candidates, name="candidates"),
    path("vote", views.castVote, name="cast_vote"),
    path("results", views.results, name="results"),
]
