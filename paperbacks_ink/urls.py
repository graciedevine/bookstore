"""Defines URL patterns for paperbacks_ink."""

from django.urls import path

from . import views

app_name = 'paperbacks_ink'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # About page
    path('about/', views.about, name='about'),
    # Kaffee Kultur page
    path('kaffee/', views.kaffee, name='kaffee'),
    # Contact Us
    path('contact/', views.contact, name='contact'),

]