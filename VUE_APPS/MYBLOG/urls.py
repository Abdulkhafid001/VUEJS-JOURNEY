# get views to map to url paths
from django.urls import path
from MYBLOG import views
# using the Django auth views function
from django.contrib.auth import views as auth_views
urlpatterns = [
    # sign up urlpath
    path('', views.sign_up, name='signupview'),
    # login url path
    path('login/', views.login, name='loginview'),
    # homepage url path
    path('home/', views.home, name='homepage'),
    # logout url path
    path('logout/', views.logout_user, name='logout'),
    # change password url
    path('changepassword/', views.change_password, name='changepassword')
]
