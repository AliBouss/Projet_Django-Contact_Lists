from django.db import models

# Create your models here.


class ContactModel(models.Model):

    fullname = models.CharField(max_length=123)
    relationship = models.CharField(max_length=123)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=123)
    address = models.CharField(max_length=123)

    def __str__(self):
        return self.fullname
