from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Post (models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    














"""
on_delete=models.PROTECT -> PROTECT prevents the deletion of the parent object if any child objects still reference it, raising a `ProtectedError`


"""