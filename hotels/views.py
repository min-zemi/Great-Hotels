from django.shortcuts import render

from .forms import HotelSearchForm


def home(request):
    return render(request, "hotels/home.html")


def hotel_search(request):
    form = HotelSearchForm()

    context = {
        "form": form,
    }

    return render(request, "hotels/search.html", context)


def hotel_search_results(request):
    form = HotelSearchForm(request.GET or None)

    hotels = []
    search_data = None

    if form.is_valid():
        search_data = form.cleaned_data

        city = search_data["city"]
        room_type = search_data["room_type"]

        # Exercise 10用の仮データ
        hotel_data = [
            {
                "name": "Aizu Grand Hotel",
                "city": "aizuwakamatsu",
                "room_type": "standard",
            },
            {
                "name": "Aizu Castle Hotel",
                "city": "aizuwakamatsu",
                "room_type": "double",
            },
            {
                "name": "Tokyo Central Hotel",
                "city": "tokyo",
                "room_type": "standard",
            },
            {
                "name": "Tokyo Bay Hotel",
                "city": "tokyo",
                "room_type": "deluxe",
            },
        ]

        hotels = [
            hotel
            for hotel in hotel_data
            if hotel["city"] == city
            and hotel["room_type"] == room_type
        ]

    context = {
        "hotels": hotels,
        "search_data": search_data,
    }

    return render(
        request,
        "hotels/partials/search_results.html",
        context,
    )


def hotel_list(request):
    return render(request, "hotels/list.html")


def register(request):
    return render(request, "hotels/register.html")


def reserve(request):
    return render(request, "hotels/reserve.html")


def success(request):
    return render(request, "hotels/success.html")