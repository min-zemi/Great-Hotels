from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("hotels/", views.hotel_list, name="hotel_list"),
    path("register/", views.register, name="register"),
    path("reserve/", views.reserve, name="reserve"),
    path("success/", views.success, name="success"),
]