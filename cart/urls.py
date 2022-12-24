from .views import cart_detail_view
from django.urls import path, include

app_name = 'cart'


urlpatterns = [

    path('', cart_detail_view, name='cart_detail'),
]
