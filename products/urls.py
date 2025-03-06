from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductApiView.as_view(), name='list'),
    path('products/<int:pk>/', views.ProductDetailApiView.as_view(), name='detail'),
]
