from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hotels/", views.hotel_list, name="hotel_list"),
    path("register/", views.register, name="register"),
    path("reserve/", views.reserve, name="reserve"),
    path("success/", views.success, name="success"),
    path("search/", views.hotel_search, name="hotel_search"),

    # HTMXで検索結果だけを取得するURL
    path(
        "search/results/",
        views.hotel_search_results,
        name="hotel_search_results",
    ),
]