from django.urls import path
from . import views


urlpatterns = [
    path('', views.signin, name= 'home'),
    path('Signup/', views.signup, name= 'Signup'),
    path('loginview/', views.loginview, name= 'loginview'),
    path('logoutview/', views.logoutview, name='logoutview'),
    path('submit/<int:pk>/result/', views.process, name= 'process'),
    path('submit/<int:pk>/', views.submit, name='submit'),
    path('quiz/', views.quiz, name='quiz'),
    ]