from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('userregi',views.regi),
    path('userlog',views.userlogin),
]