from django.urls import path
from housing import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('properties', views.properties, name='properties'),
    path('blog', views.blog, name='blog'),
]

