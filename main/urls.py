from django.urls import path
from . import views
from .views import PostDetailView, MainView, SignUpView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('blog/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('card/', views.card, name='card'),
    # path('article/', views.article, name='article'),
    path('contacts/', views.contacts, name='contacts'),
    path('contacts/thanks/', views.thanks, name='thanks'),
    path('registration/', views.registration, name='registration'),
]
