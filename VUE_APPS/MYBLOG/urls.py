# get views to map to url paths
from django.urls import path
from MYBLOG import views
urlpatterns = [
    path('', views.login, name='loginView'),
]
