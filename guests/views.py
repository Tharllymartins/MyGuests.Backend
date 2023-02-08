from django.shortcuts import render


def guest_register(request):
    context = {
        
    }
    
    return render(request, "registrar_visitante.html", context)