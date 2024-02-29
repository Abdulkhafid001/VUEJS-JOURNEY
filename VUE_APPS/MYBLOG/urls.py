# get views to map to url paths
from django.urls import path
from MYBLOG import views
# using the Django auth views function
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.django_auth, name='signupview'),
    path('login', views.django_login, name='loginview'),
    path('home/', views.home, name='homepage'),
    path('logout/', views.home, name='logout'),
]
