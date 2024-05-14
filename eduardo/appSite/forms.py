from django import forms
from django.forms import ModelForm
from .models import Itens

class ItensForm(forms.ModelForm):
    class Meta:
        model = Itens
        fields = "__all__"
        labels = {
            'nome': "identificação",
            'email': "endereço",
        }
        widgets = {
            'nome' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Ex João",
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Ex joao@gmail.com",
                }
            )
        }
