from django.urls import path
from . import views

urlpatterns = [
    path('climatologia/', views.vista_climatologica, name='vista_climatologica'),
]
