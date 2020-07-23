from django.urls import path
from Four_App import views

#Template tagging
#This is used to reference on html pg
app_name = 'Four_App'

urlpatterns = [
    path('schools/',views.SchoolListView.as_view(),name="list"),
    path('schools/<int:pk>/', views.SchoolDetailView.as_view(),name='detail'),
    path('create/', views.SchoolCreateView.as_view(),name="create"),
    path('update/<int:pk>/', views.SchoolUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/', views.SchoolDeleteView.as_view(),name='delete'),
]

#EXAMPLE OF URL PATTERNS
# urlpatterns = [
#     path('users/', views.users,name='users'),
#     path('other/', views.other,name='other'),
#     path('relative/', views.relative,name='relative_url_templates'),
#     path('register/', views.register, name='register'),
#     path('user_login/',views.user_login,name="user_login"),
#     path('school_detail/',views.SchoolDetailView.as_view(),name="detail"),
# ]
