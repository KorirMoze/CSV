from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   
    path('',views.csvr,name='csv'),
    path('upload/', views.upload_csv, name='upload'),
]
