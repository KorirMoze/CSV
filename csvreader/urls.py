from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   
    path('',views.csvr,name='csv'),
    path('upload/', views.upload_csv, name='upload'),
    path('oauth/success', views.oauth_success, name='test_oauth_success'),
    path('stk-push/success', views.stk_push_success, name='test_stk_push_success'),
]
