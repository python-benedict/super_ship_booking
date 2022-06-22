from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.passengerRegister, name='register'),
    path('<int:id>/', views.update, name='update'),
    path('del/<int:id>/', views.delete, name='delete'),
    path('passengerList/', views.passengerList, name='passengerList'),
]