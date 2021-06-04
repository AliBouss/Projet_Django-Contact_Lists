from django.urls import path
from contactlist.views import *

urlpatterns = [
    path('', index, name='index'),
    path('add-contact/', addcontact, name='add-contact'),
    path('edit/<str:pk>', edit, name='edit'),
    path('profile/<str:pk>', contactProfile, name='profile'),
    path('delete/<str:pk>', delete, name='delete'),
]
