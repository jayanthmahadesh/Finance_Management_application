from django.db import models
from django.contrib.auth.models import Permission
from django.core.validators import MinValueValidator

# Create your models here.

class expense(models.Model):
    name = models.CharField(max_length=140)
    value = models.IntegerField()
    # value = models.PositiveIntegerField(validators=[MinValueValidator(0)],editable=false
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    def __str__(self):
        return self.name