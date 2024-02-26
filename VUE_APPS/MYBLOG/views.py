from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from MYBLOG.models import UserDetails
from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('userName')
        pass_word = request.POST.get('passWord')
        # save the details to the userDetails database
        user = UserDetails(user_name=user_name, pass_word=pass_word)
        # save the details
        user.save()
    mydata = UserDetails.objects.all().values()
    # template = loader.get_template('login.html')
    context = {'users': mydata, }
    # print(user_name, pass_word)
    # return HttpResponse(template.render(), context)
    # return render(request, "login.html", context=context)

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
    return render(request, "login.html", context=context)
