from django.http import HttpResponse

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