from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
    
def pagina(request):
    variavel = ["Item 1", "Item 2", "Item 3"]
    return render(request, 'index.html', {'variavel': variavel})
