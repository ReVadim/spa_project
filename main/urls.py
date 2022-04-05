from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('card/', views.card, name='card'),
    path('article/', views.article, name='article'),
    path('contacts/', views.contacts, name='contacts'),
    path('contacts/thanks/', views.thanks, name='thanks'),
    path('registration/', views.registration, name='registration'),
    path('signup/', views.signup, name='signup'),
]
