from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

x = "oi"
    
def pagina(request):
    return render(request, x)