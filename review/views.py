from django.shortcuts import render,redirect

from .models import Post

# Create your views here.



def home(request):

	a=Post.objects.all()

	return render(request, 'review/home.html',{'a':a})