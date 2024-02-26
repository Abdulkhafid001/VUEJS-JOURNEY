# get views to map to url paths
from django.urls import path
from MYBLOG import views
urlpatterns = [
    path('', views.django_auth, name='loginView'),
]
