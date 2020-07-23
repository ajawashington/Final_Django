from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=100)
    principal_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Four_App:detail",kwargs={'pk':self.pk})

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


#MODEL BULDING EXAMPLES

#After you create models register them in admin.py

# class User(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=128, unique=True)

#pip install pillow --- need for image upload
# class UserProfileInfo(models.Model):
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional classes
    # portfolio_site = models.URLField(blank=True)
    # profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    #
    # def __str__(self):
    #     return self.user.username
