from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login, logout
# Create your views here.
from myblog.models import password_change_request
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from myblog.mycode import AppUtilities


# using the django built in authentication system


def sign_up(request):
    if request.method == 'POST':
        user_name = request.POST['userName']
        user_pass_word = request.POST['passWord']
        user_email = request.POST['userEmail']
        # use the django admin User model
        new_user = User.objects.create_user(
            username=user_name, email=user_email, password=user_pass_word)
        # save user instance
        new_user.save()
        redirect(home)
    return render(request, "signup.html")

# Django log in using GET http method


@login_required
def home(request):
    # get all the saved users in the User database
    my_users = User.objects.all().values()
    context = {'myUsers': my_users}
    return render(request, "home.html", context=context)


def logout_user(request):
    logout(request)
    return redirect(sign_up)

# use GET for websearch not password retrieve


def login(request):
    if request.method == 'POST':
        user_name = request.POST['userName']
        user_pass_word = request.POST['passWord']
        # print(user_name, user_pass_word)
        # user_email = request.POST['userEmail']
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
    if request.method == 'POST':
        user_mail = request.POST['userMail']
        utilities = AppUtilities()
        random_key = utilities.generate_secret_key(16)
        # check if mail is DB
        user1 = User.objects.get(email=user_mail)
        # save user to DB
        password_db = password_change_request(
            user_random_key=random_key, mail_of_user=user1.email)
        password_db.save()
        # send mail to user
        email = EmailMessage(f"change password for {
                             user1.username}", f"click this link to reset your password: http://127.0.0.1:8000/setpassword/{random_key}", to=[user1.email])
        email.send(fail_silently=False)
        # context1 = {'message': message}
    return render(request, 'forgotpassword.html')


def check_secret_key(request, key):
    # check if key in changepassword DB
    message = 'Fake URL path!'
    if password_change_request.DoesNotExist:
        message = 'proceed to change password'
        # redirect to change password page
        # return redirect(change_password)
    else:
        user_in_db = password_change_request.objects.get(user_random_key=key)
        message = 'user in db please set a new password'
    return render(request, 'setpassword.html', {'message': message})
