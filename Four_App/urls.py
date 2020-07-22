from django.urls import path
from Four_App import views

urlpatterns = [
    path('', views.users,name='users'),

]
