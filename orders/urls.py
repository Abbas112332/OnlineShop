from .views import order_create_view
from django.urls import path, include

urlpatterns = [

    path('create/', order_create_view, name='order_create'),

]
