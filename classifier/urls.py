from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from classifier import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='classifier/home.html'), name='home'),
    path('pos/', views.pos, name='pos'),
    path('history/', views.history_list, name='history'),
    path('about/', views.about, name='about'),
    path('live/', views.live, name='live'),
    path('topics/', views.topics_list, name='topics'),
    path('post/<int:pk>', views.usertext_detail, name='corpus_detail'),

]