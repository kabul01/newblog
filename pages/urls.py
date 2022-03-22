from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePagesView.as_view(), name='home')
]
