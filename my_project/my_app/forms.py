from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Aplicatie, Endpoint, Bug, SetariUtilizator

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numele...', 'autocomplete':'off'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email...', 'autocomplete':'off'}),
        }

class AplicatieForm(forms.ModelForm):
    class Meta:
        model = Aplicatie
        fields = '__all__'
        widgets = {
            'user':forms.TextInput(attrs={'class':'form-control', 'id':'user1', 'value':'', 'type':'hidden', 'name':'user'}),
            'nume':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numele aplicatiei...'}),
            'descriere':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descriere...'}),
            'stare':forms.TextInput(attrs={'class':'form-control'}),
        }

class EndpointForm(forms.ModelForm):
    class Meta:
        model = Endpoint
        fields = '__all__'
        widgets = {
            'user':forms.TextInput(attrs={'class':'form-control', 'id':'user1', 'value':'', 'type':'hidden', 'name':'user'}),
            'aplicatie':forms.TextInput(attrs={'class':'form-control', 'id':'aplicatie1', 'value':'', 'type':'hidden', 'name':'aplicatie'}),
            'nume': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nume Endpoint...'}),
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder':'Url...'}),
            'metoda_http': forms.Select(attrs={'class': 'form-control'}),
            'stare':forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
        }

class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('user', 'aplicatie', 'descriere')
        widgets = {
            'user':forms.TextInput(attrs={'class':'form-control', 'id':'user1', 'value':'', 'type':'hidden', 'name':'user'}),
            'aplicatie':forms.TextInput(attrs={'class':'form-control', 'id':'aplicatie1', 'value':'', 'type':'hidden', 'name':'aplicatie'}),
            'descriere':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Raporteaza Bug...'}),
        }

class SetariForm(forms.ModelForm):
    class Meta:
        model = SetariUtilizator
        fields = ['interval_verificare']
        widgets = {
            'interval_verificare':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Interval verificare...'})
        }