from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('test', test, name='test'),
    path('get_quote', get_quote, name='get-quote'),
]
