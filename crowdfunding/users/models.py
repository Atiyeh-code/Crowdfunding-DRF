from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models

class CustomUser(AbstractUser):
    # pass
    first_name = models.CharField(max_length=30, verbose_name='first name')
    last_name = models.CharField(max_length=100, verbose_name='last name')
    image = models.URLField(max_length=200, verbose_name='profile photo', default='https://flyinryanhawks.org/wp-content/uploads/2016/08/profile-placeholder.png')
    location = models.CharField(max_length=100, verbose_name='location', default = 'Brisbane')

    def __str__(self):
        return self.username

