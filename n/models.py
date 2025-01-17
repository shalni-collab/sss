from django.db import models
class contact(models.Model):
    email=models.EmailField(null=True)
    password=models.CharField(max_length=50,null=True)

# Create your models here.


  
