from django import forms
from app1.models import stud


class studentForm (forms.ModelForm):

   class Meta:
        model = stud
        fields = '__all__'  
