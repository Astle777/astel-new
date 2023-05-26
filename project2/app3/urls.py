
from django.urls import path
from app2 import views

urlpatterns = [
    path('',views.home,name='home'),
    path("home2/",views.home2,name="home2"),
]
