from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from MYBLOG.models import UserDetails


# using the django built in authentication system


def django_auth(request):
    if request.method == 'POST':
        user_name = request.POST.get('userName')
        user_pass_word = request.POST.get('passWord')
        user_email = request.POST.get('userEmail')
        # use the django admin User model
        new_user = User.objects.create_user(
            username=user_name, email=user_email, password=user_pass_word)
        # save user instance
        new_user.save()
    # get all the saved users in the User database
    my_users = User.objects.all().values()
    context = {'myUsers': my_users, }
    return render(request, "signup.html", context=context)
