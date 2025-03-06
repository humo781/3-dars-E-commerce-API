from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.OrderApiView.as_view(), name='list'),
    path('orders/<int:pk>/', views.OrderDetailApiView.as_view(), name='detail'),
]
