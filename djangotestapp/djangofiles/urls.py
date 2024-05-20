from django.contrib import admin
from django.urls import path, include
from two_factor.urls import urlpatterns as tf_urls # import two_factor url patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")), # path to the debug toolbar
    # path("/oldroute", include('myblog.urls')),# route the auth app URLCOnf
    path("", include("blogger.urls")), # route to new blogger app
    path('', include(tf_urls)),
]
