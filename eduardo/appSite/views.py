from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
# Create your views here.
    
def pagina(request):
    form = ItensForm
    if request.method == "POST":
        form = ItensForm(request.POST)
        if form.is_valid():
            form.save
    variavel = ["Item 1", "Item 2", "Item 3"]
    return render(request, 'index.html', {'variavel': variavel, "form":form})
    