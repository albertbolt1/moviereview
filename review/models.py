from django.db import models

# Create your models here.


class Post(models.Model):
	moviename = models.CharField(max_length= 50)
	stars=models.CharField(max_length= 50,default="no stars")
	picture =models.ImageField(upload_to='images/')
	review=models.CharField(max_length=1000)

