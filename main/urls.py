from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import PostDetailView, MainView, SignUpView, SignInView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('blog/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout', ),
    # path('card/', views.card, name='card'),
    # path('article/', views.article, name='article'),
    path('contacts/', views.contacts, name='contacts'),
    path('contacts/thanks/', views.thanks, name='thanks'),
    path('registration/', views.registration, name='registration'),
]
