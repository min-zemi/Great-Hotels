from django.http import HttpResponse
from django.shortcuts import render
from .forms import HotelSearchForm


def hotel_search(request):
    form = HotelSearchForm(request.GET or None)

    search_data = None

    if form.is_valid():
        search_data = form.cleaned_data

    context = {
        "form": form,
        "search_data": search_data,
    }

    return render(request, "hotels/search.html", context)


def home(request):
    return render(request, "hotels/home.html")


def hotel_list(request):
    return render(request, "hotels/list.html")


def register(request):
    return render(request, "hotels/register.html")


def reserve(request):
    return render(request, "hotels/reserve.html")


def success(request):
    return render(request, "hotels/success.html")