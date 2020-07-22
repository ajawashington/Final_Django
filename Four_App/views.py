from django.shortcuts import render
from Four_App.models import User
from Four_App import forms

# Create your views here.


def index(request):
    return render(request, 'Four_App/index.html')

# it is not possible to render two views to the same url
#so we compressed the getAll() and the  post for new users into one view

#MODEL FORM!
#this var will be used to pass through urls.py
def users(request):
    #create an new user form to be populated
    form = forms.NewUserForm()

    #on submit, here is the post request to that form
    if request.method == 'POST':
     form = forms.NewUserForm(request.POST)

     #if valid that post will save to the database
    if form.is_valid():
            form.save(commit=True)
            return index(request)

    else:
            print('ERROR FORM INVALID')

    #here is the dictionary for the user list
    mv = User.objects.all().order_by('first_name')

    #context of the view is being defined here included the NewUserForm and the UserList
    #form and user_list are the template tags
    context = {'form': form, 'user_list': mv}

    #return full context
    return render(request,'Four_App/users.html', context)

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



def other(request):
    return render(request, 'Four_App/other.html')

def relative(request):
    return render(request, 'Four_App/relative_url_templates.html')
