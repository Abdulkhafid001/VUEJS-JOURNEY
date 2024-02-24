from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from MYBLOG.models import UserDetails
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('userName')
        pass_word = request.POST.get('passWord')
        # save the details to the userDetails database
        user = UserDetails(user_name=user_name, pass_word=pass_word)
        # save the details
        user.save()
    mydata = UserDetails.objects.values_list('user_name')
    template = loader.get_template('login.html')
    context = {'users': mydata}
    # print(user_name, pass_word)
    return HttpResponse(template.render())
