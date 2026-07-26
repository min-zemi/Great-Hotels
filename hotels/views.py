from django.http import HttpResponse

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
    return HttpResponse("Hotel Booking Home")

def hotel_list(request):
    return HttpResponse("Matching Hotels")

def register(request):
    return HttpResponse("User Registration")

def reserve(request):
    return HttpResponse("Reservation Completed")

def success(request):
    return HttpResponse("Booking Success")
