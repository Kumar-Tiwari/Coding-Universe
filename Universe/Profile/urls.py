from django.urls import path
from .views import ProfileView

urlpatterns=[
    path('<str:name>',ProfileView,name='profile'),
]