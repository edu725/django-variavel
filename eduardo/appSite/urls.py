from django.urls import path

from . import views

urlpatterns = [
    path("pagina/", views.pagina, name="pagina")
]