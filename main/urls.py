from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('test/', test, name='test'),
    path('get_quote/', get_quote, name='get-quote'),
    path('about/', about, name='about'),
    path('blog_single/', blog_single, name='blog-single'),
    path('blog/', blog, name='blog'),
    path('doctors/', doctors, name='doctors'),
    path('services/', services, name='services'),
]