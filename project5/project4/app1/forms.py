from django import forms
from app1.models import collage

class studentform(forms.ModelForm):
    class Meta:
        model=collage
        fields ='__all__'