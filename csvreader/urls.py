from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   
    # path('',views.csvr,name='csv'),
    path('upload/', views.upload_csv, name='upload'),
    path('oauth/success', views.oauth_success, name='test_oauth_success'),
    path('stk-push/success', views.stk_push_success, name='test_stk_push_success'),
    
    path('message/',views.message, name='message'),
	# path('c2b/validation/', views.c2b_validation),
    path('c2b/', views.c2b_confirmation, name='c2b'),
    # path('register/',views.register_c2b_url,name='register'),
    path('register_urls/',views.register_urls,name='register_urls'),
    # path('validation/',views.validation,name='validation')
]
