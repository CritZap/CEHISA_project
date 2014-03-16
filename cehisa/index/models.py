from django.db import models
from django.contrib.auth.models import User

class Menu(models.Model):
    text = models.CharField(max_length=200)

