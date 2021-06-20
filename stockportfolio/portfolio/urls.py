from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "home"),
    path('delete/<stock_name>/', views.delete_stock, name='delete_stock'),
]
