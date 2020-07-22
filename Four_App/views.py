from django.shortcuts import render
from Four_App.models import User
from Four_App import forms

# Create your views here.

def index(request):
    return render(request, 'Four_App/index.html')

def users(request):

    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request,'Four_App/users.html', context=user_dict)

def form_name_view(request):
    form = forms.Form_Name()


    if request.method == 'POST':
        form = forms.Form_Name(request.POST)

        if form.is_valid():
            print('validation success!')
            print('Name:' +form.cleaned_data['name'])
            print('Description:' +form.cleaned_data['description'])
            print('Text:' +form.cleaned_data['text'])

    return render(request, 'Four_App/form_page.html', {'form': form})
