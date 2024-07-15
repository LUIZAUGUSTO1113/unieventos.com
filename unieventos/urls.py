from django.urls import path
from . import views

app_name = 'unieventos'

# urls do app unieventos
urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('events/<int:pk>', views.event_detail, name='event_detail'),
    path('create/', views.create_event, name='create'),
    path('about/', views.about, name='about'),
]