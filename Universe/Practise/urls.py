from django.urls import path
from .views import PractiseView,Result

urlpatterns=[
    path('',PractiseView,name='practise'),
    path('result/',Result,name='result'),
]