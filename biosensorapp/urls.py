from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get-users/', views.get_users_data),
    path('get-sensor-data/', views.get_sensor_data),

    
]