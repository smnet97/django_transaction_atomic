from django.urls import path
from .views import registration_view

urlpatterns = [
    path('sign-up/', registration_view, name='register'),
]