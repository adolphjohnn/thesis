from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from . models import QuestionAnswer

class ProductForm(forms.ModelForm):
    class Meta:
        model = QuestionAnswer
        fields = '__all__'