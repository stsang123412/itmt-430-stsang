from django.db import models
from django.contrib.auth.models import User
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)
from django_currentuser.db.models import CurrentUserField
import django.utils.timezone

# Create your models here.


class Post(models.Model):
    date_posted = models.DateTimeField(default=django.utils.timezone.now)
    name = CurrentUserField()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    content = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
