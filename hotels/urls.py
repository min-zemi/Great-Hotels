from django.urls import path

from . import views

urlpatterns = [
    path("search/", views.hotel_search, name="hotel_search"),
]