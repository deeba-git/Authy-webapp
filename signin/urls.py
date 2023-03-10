from django.urls import path
from . import views

app_name = 'sign_in'

urlpatterns = [
    path('', views.signin, name='signin'),
    path('', views.auth_user, name='load_db'),
    path('', views.logout, name='logout'),
]
