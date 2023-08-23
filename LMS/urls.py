from django.urls import path
from .views import *

urlpatterns = [
    path('', view_home, name='home'),
    path('secure1', view_secure1, name='secure1'),
    path('secure2', view_secure2, name='secure2'),
    path('unsecure1', view_unsecure1, name='unsecure1'),
    path('unsecure2', view_unsecure2, name='unsecure2'),
    path('logout/', view_logout, name='logout'),
]