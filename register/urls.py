from django.contrib import admin
from django.urls import path, include

from register import views

urlpatterns = [
   path('', views.signup, name='signup'),
]