from django.db import models
from django.contrib.auth.models import Permission
from django.core.validators import MinValueValidator

# Create your models here.

class expense(models.Model):
    name = models.CharField(max_length=140) #name of the expence
    value = models.IntegerField()           #amount spent in this expence
    description = models.CharField(max_length=100) 
    category = models.CharField(max_length=20) 
    date = models.DateField()               #date of the expence
    created_at = models.DateTimeField(auto_now_add=True) #when the recorded is added
    updated_at = models.DateTimeField(auto_now=True) #date and time when record is updated
    created_by = models.CharField(max_length=100) #username who added the record
    def __str__(self):
        return self.name