from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserDetails(models.Model):
    user_name = models.CharField(max_length=100, null=False)
    pass_word = models.CharField(max_length=100, null=False)


# chnage password request model
class password_change_request(models.Model):
    user_random_key = models.CharField(max_length=50, null=False)
    mail_of_user = models.CharField(max_length=50, null=False)

