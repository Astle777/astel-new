from django import forms
from app1.models import Book


class Books(forms.ModelForm):
    class Meta:
        model =Book
        fields='__all__'