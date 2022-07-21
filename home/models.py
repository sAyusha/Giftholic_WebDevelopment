from email import message
from django.db import models
from django.conf import settings

# Create your models here.
class Contact(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(default=" ")
    def __str__(self):
        return self.fullname
