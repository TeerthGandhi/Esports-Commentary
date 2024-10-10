# users/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Your URL patterns for the users app go here
    path('', views.index, name='index'),
    path('upload', views.upload, name='upload'),

]


