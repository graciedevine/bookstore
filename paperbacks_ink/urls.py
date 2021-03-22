"""Defines URL patterns for paperbacks_ink."""

from django.urls import path

from . import views

app_name = 'paperbacks_ink'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Events page
    path('about/', views.events, name='events'),
    # Kaffee Kultur page
    path('kaffee/', views.kaffee, name='kaffee'),
    # Contact Us
    path('contact/', views.contact, name='contact'),

]