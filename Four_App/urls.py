from django.urls import path
from Four_App import views

#Template tagging
#This is used to reference on html pg
app_name = 'Four_App'

urlpatterns = [
    path('register/', views.register, name='register'),
]







#EXAMPLE OF URL PATTERNS
# urlpatterns = [
#     path('users/', views.users,name='users'),
#     path('other/', views.other,name='other'),
#     path('relative/', views.relative,name='relative_url_templates'),
# ]
