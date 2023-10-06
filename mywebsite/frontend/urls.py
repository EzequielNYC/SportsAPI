from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('use_api/', views.api_token, name='use_api'),
    path('contact/', views.contact, name='contact'),
    path('data_preview/', views.data_preview, name='data_preview'),
]
