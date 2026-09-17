from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lineup/', views.lineup, name='lineup'),
    path('truck/<int:pk>/', views.truck_detail, name='truck_detail'),
    path('trucks/<int:pk>/', views.truck_detail, name='truck_detail_alias'),    
    path('technology/', views.technology, name='technology'),
    path('quote/', views.get_quote, name='get_quote'),
] 