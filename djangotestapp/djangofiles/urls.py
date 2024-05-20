from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path to the debug toolbar
    path("__debug__/", include("debug_toolbar.urls")),
    # route the auth app URLCOnf
    # path("/oldroute", include('myblog.urls')),
    # route to new blogger app
    path("", include("blogger.urls"))
]
