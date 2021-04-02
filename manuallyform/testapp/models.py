from django.db import models

# Create your models here.
class User(models.Model):
    
    email = models.EmailField(max_length=70)
    passward = models.CharField(max_length=70)

    def __str__(self):
        return self.email



        

