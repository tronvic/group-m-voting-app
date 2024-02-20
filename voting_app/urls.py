from django.urls import path

from . import views

app_name = 'voting_app'  # Specify the app name

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('vote/', views.vote_view, name='vote'),
    path('results/', views.results_view, name='results'),
    ]