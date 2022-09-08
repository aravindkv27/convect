from django.urls import path
from . import views

urlpatterns = [

    path('',views.home, name = 'aravind'),
    # path('home/', views.home, name='aravind'),
    path('rooms/<str:pk>/', views.room, name='room')
]