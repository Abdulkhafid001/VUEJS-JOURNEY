from django.contrib import admin
from MYBLOG.models import UserDetails, password_change_request
# Register your models here.
admin.site.register(UserDetails)
admin.site.register(password_change_request)
