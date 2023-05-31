from app1.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from app1.models import Employees
from django import forms
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields =UserCreationForm.Meta.fields+('email','phone')
        
        
class Employee(forms.ModelForm):
    class Meta:
        model =Employees
        fields='__all__'