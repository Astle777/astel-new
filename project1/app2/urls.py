from app2 import views
from django.urls import path
urlpatterns = [
    path('Django2/',views.home,name='home'),
    path('home1/',views.home3,name='home1'),
    path('home2/',views.home1,name="home2"),
]
