from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_product, name='all_product'),
]