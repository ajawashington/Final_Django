# Create your views here.
#each view must have a url pattern in urls.py
from django.shortcuts import render
from . import models
from django.urls import reverse_lazy
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,UpdateView,
                                DeleteView)


class SchoolListView(ListView): #<!-- list view returns the model lowercased and add _list -->
    model = models.School
    # context_oject_name = 'schools'  #defining the context yourself


class SchoolDetailView(DetailView): #detail view returns the model lowercased
    model = models.School
    template_name = 'Four_App/school_detail.html'
    context_object_name = 'school_detail'

class IndexView(TemplateView):
    template_name = 'Four_App/index.html'

    def get_context_data(self, **kwargs): #keyword arguments
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'
        return context

class SchoolCreateView(CreateView):
    fields = ('name', 'principal_name', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal_name')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("Four_App:list")









#CBV Imports
# from django.views.generic import View, TemplateView
# from django.http import HttpResponseRedirect, HttpResponse
# from django.urls import reverse

#Class Based Views
# class CBView(View):
#     def get(self, request):
#         return HttpResponse("CLASS BASED VIEWS!")



# #AUTH IMPORTS
# from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.decorators import login_required
# from Four_App.forms import UserForm, UserProfileInfoForm
#
# #AUTH EXAMPLE
# @login_required
# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('IndexView'))
#
# @login_required
# def special(request):
#     return HttpResponse('You are logged in!')
#
# def register(request):
#
#         registered = False
#
#         if request.method == 'POST':
#             user_form = UserForm(data=request.POST)
#             profile_form = UserProfileInfoForm(data=request.POST)
#
#             if user_form.is_valid() and profile_form.is_valid():
#
#                     user = user_form.save()
#                     user.set_password(user.password)
#                     user.save()
#
#                     profile = profile_form.save(commit=False)
#                     profile.user = user
#
#                     if 'profile_pic' in request.FILES:
#
#                         profile.profile_pic = request.FILES['profile_pic']
#
#                     profile.save()
#                     registered = True
#             else:
#                     print(user_form.errors,profile_form.errors)
#         else:
#             user_form = UserForm()
#             profile_form = UserProfileInfoForm()
#
#         return render(request, 'Four_App/register.html',
#                     {'user_form': user_form,
#                     'profile_form':profile_form,
#                     'registered':registered})
#
# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         user = authenticate(username=username,password=password)
#
#         if user:
#             if user.is_active:
#                 login(request,user)
#                 return HttpResponseRedirect(reverse('IndexView'))
#
#             else:
#                 return HttpResponse('Account Not Active')
#         else:
#             print("Someone logged in and failed!")
#             print("Username: {} and password: {}".format(username,password))
#             return HttpResponse("Invalid Login Details")
#     else:
#         return render(request, 'Four_App/login.html',{})


#VIEW NOTES!

# # it is not possible to render two views to the same url
# #so we compressed the getAll() and the  post for new users into one view
# from Four_App.models import User
#
#VIEWS!
# #this var will be used to pass through urls.py

# def index(request):
#     return render (request, 'Four_App/index.html')

# def index(request):
#     context_dict = {'text': 'hello world', 'number':100}
#     return render(request, 'Four_App/index.html', context_dict)

# def users(request):
#     #create an new user form to be populated
#     form = forms.NewUserForm()
#
#     #on submit, here is the post request to that form
#     if request.method == 'POST':
#      form = forms.NewUserForm(request.POST)
#
#      #if valid that post will save to the database
#     if form.is_valid():
#             form.save(commit=True)
#             return index(request)
#
#     else:
#             print('ERROR FORM INVALID')
#
#     #here is the dictionary for the user list
#     mv = User.objects.all().order_by('first_name')
#
#     #context of the view is being defined here included the NewUserForm and the UserList
#     #form and user_list are the template tags
#     context = {'form': form, 'user_list': mv}
#
#     #return full context
#     return render(request,'Four_App/users.html', context)
#
# def form_name_view(request):
#     form = forms.Form_Name()
#
#     if request.method == 'POST':
#         form = forms.Form_Name(request.POST)
#
#         if form.is_valid():
#             print('validation success!')
#             print('Name:' +form.cleaned_data['name'])
#             print('Description:' +form.cleaned_data['description'])
#             print('Text:' +form.cleaned_data['text'])
#
#     return render(request, 'Four_App/form_page.html', {'form': form})

# def other(request):
#     return render(request, 'Four_App/other.html')
#
# def relative(request):
#     return render(request, 'Four_App/relative_url_templates.html')
