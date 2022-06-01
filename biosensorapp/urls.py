from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # to get all the users from db
    path('get-users/', views.get_users_data),
    # to get sensor data for selected user
    path('get-sensor-data/', views.get_sensor_data),
    # to insert sensor data from mobile app
    path('insert-data-from-mobile/', views.insert_data_from_mobile),
    # to get the latest test date from the db, for a particular test type of a user
    path('get-last-test-details/', views.get_last_test_details),


    # for user login
    path('user-login/', views.user_login),
    # for user logout
    path('user-logout/', views.user_logout),
    # for checking session, this would help  before loading login page
    path('check-session/', views.check_session)

]