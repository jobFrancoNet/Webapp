from django.db import models

# Create your models here.

class Leccespesa_users(models.Model):
    email = models.CharField(max_length=30)
    password_user = models.CharField(max_length=30)
