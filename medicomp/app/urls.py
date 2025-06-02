from django.urls import path
from . import views

urlpatterns = [
    path('', views.remedy_compare, name='remedy_compare'),
]