from django import forms
from .models import Game
from django.contrib.auth.forms import UserCreationForm
from django_select2 import forms as s2forms


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'rating', 'genre', 'platform', 'developingCompany')

