from django.shortcuts import render
from guests.models import Guest


def index(request):
    
    qs_guests = Guest.objects.all()
    
    context = {
        "guests": qs_guests
    }
    
    return render(request, "index.html", context)