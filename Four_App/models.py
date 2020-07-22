from django.db import models

# Create your models here.
#After you create models register them in admin.py

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=128, unique=True)
