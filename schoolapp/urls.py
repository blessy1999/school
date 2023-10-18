from . import views
from django.urls import path
urlpatterns = [
    path('', views.school, name='school'),
    path('login', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('home', views.home, name='home'),
    path('success', views.success_page, name='success_page'),
]
