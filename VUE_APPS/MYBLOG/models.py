from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserDetails(models.Model):
    user_name = models.CharField(max_length=100, null=False)
    pass_word = models.CharField(max_length=100, null=False)


# using  the DJnago docs to build an authentication system
# use the create user method to create a user object
user = User('codeX', 'Abdul123', 'kabiruabdulkhafid@gmail.com')
