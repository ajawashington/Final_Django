from django.shortcuts import render
from Four_App.models import User

# Create your views here.

def index(request):
    return render(request, 'Four_App/index.html')

def users(request):

    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request,'Four_App/users.html', context=user_dict)
