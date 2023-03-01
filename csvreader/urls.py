from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   
    path('',views.csvr,name='csv'),
    path('upload-csv/', upload_csv, name='upload_csv'),
]
