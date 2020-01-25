from django.db import models

# Create your models here.


class Post(models.Model):
	moviename = models.CharField(max_length= 50)
	stars=models.CharField(max_length= 50,default="no stars")
	picture =models.URLField(max_length=200)
	review=models.CharField(max_length=1000)


class Bigreview(models.Model):
	post=models.ForeignKey(Post, on_delete=models.CASCADE)
	review1=models.CharField(max_length=1000)


