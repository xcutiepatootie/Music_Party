from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField(null=False, max_length=25)
    age = models.IntegerField(null=False)
    email = models.EmailField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name