from django.urls import path
from .views import Home,Search

urlpatterns=[
    path('',Home,name='home'),
    path('s/',Search,name='search'),
]