from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email

class Partnership(models.Model):
    name = models.CharField(max_length=120)
    business_name = models.CharField(max_length = 200)
    email = models.EmailField()
    phone_no = models.CharField(max_length = 14)
    message = models.TextField()

    
