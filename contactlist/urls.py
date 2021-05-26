from django.urls import path
from contactlist.views import *

urlpatterns = [
    path('', index, name='index'),
    
]