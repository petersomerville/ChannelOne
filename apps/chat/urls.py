from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('room/<str:room_name>', views.index, name='index'),
    path('create/', views.create_room, name='create_room'),
]