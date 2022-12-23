from .views import ProductListView, ProductDetailView
from django.urls import path, include

urlpatterns = [

    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail')
]