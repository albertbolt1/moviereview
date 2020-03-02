from django.db import models
from django.utils.timezone import now

# Create your models here.


class Post(models.Model):
	moviename = models.CharField(max_length= 50)
	stars=models.CharField(max_length= 50,default="no stars")
	picture =models.URLField(max_length=200)
	review=models.CharField(max_length=1000)
	rating=models.IntegerField(default=0)
	review=models.CharField(max_length=1000)
	release_date=models.DateTimeField(default=now,blank=True)
	genre=models.CharField(max_length=15,default="sci-fi")


class Bigreview(models.Model):
	post=models.ForeignKey(Post, on_delete=models.CASCADE)
	review1=models.CharField(max_length=1000)