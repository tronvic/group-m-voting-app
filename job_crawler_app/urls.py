from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("history", views.jobHistoryView, name="history"),
    path("portfolio", views.portfolioView, name="portfolio"),
    path("job-request", views.requestJobView, name="request"),
]
