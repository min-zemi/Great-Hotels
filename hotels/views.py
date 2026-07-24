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