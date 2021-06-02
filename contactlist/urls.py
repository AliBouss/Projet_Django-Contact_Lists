from django.urls import path
from contactlist.views import *

urlpatterns = [
    path('', index, name='index'),
    path('add-contact/', addcontact, name='add-contact'),
    path('edit/', edit, name='edit'),
    path('profile/<str:pk>', contactProfile, name='profile'),
]
