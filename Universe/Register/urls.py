from django.urls import path
from .views import SignupView,ActivateView,LoginView
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('',SignupView,name='signup'),
    path('activate/',ActivateView,name='activate'),
    path('login/',LoginView,name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
]