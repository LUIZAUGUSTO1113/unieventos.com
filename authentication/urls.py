from django.urls import path
from . import views

app_name = 'authentication'

# urls do app authentication
urlpatterns = [
    path('', views.index, name='redirect'),
    path('welcome', views.welcome, name='authentication'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
]