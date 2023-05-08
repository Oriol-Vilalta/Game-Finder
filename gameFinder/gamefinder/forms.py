from django import forms
from .models import Game
from django.contrib.auth.forms import UserCreationForm


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'rating', 'genre', 'platform', 'developingCompany')

