from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('registration', views.registration, name='registration'),
    path('login_user', views.login_user, name='login_user'),
    path('login_page', views.login_page, name='login_page'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('tests',views.tests,name='tests'),
    path('testme', views.testme, name='testme'),
]