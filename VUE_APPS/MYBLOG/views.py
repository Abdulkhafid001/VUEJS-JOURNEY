from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login, logout
# Create your views here.
from MYBLOG.models import UserDetails


# using the django built in authentication system


def sign_up(request):
    if request.method == 'POST':
        user_name = request.POST.get('userName')
        user_pass_word = request.POST.get('passWord')
        user_email = request.POST.get('userEmail')
        # use the django admin User model
        new_user = User.objects.create_user(
            username=user_name, email=user_email, password=user_pass_word)
        # save user instance
        new_user.save()

    return render(request, "signup.html")

# Django log in using GET http method


def home(request):
    # get all the saved users in the User database
    my_users = User.objects.all().values()
    context = {'myUsers': my_users, }
    return render(request, "home.html", context=context)


def logout_user(request):
    logout(request)
    return redirect(sign_up)

# use GET for websearch not password retrieve


def login(request):
    if request.method == 'POST':
        user_name = request.POST['userName']
        user_pass_word = request.POST['passWord']
        print(user_name, user_pass_word)
        user_email = request.GET.get('userEmail')
        # check if user is authenticated and redirect to homepage
        user = authenticate(request, username=user_name,
                            password=user_pass_word)
        # if user is found redirect to homepage
        if user is not None:
            # log user in
            django_login(request, user)
            return redirect(home)
        else:
            return HttpResponse("incorrect username or password. try again")
    return render(request, "login.html")

# change password view


def change_password(request):
    return render(request, 'forgotpassword.html')
