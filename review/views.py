from django.shortcuts import render,redirect,get_object_or_404


from .models import Post

# Create your views here.



def home(request):

	a=Post.objects.all().order_by('-release_date')

	return render(request, 'review/home.html',{'a':a})

def start(request):

	a=Post.objects.all().order_by('-release_date')

	return render(request, 'review/start.html',{'a':a})

def bigreview(request,post_id):
	post = get_object_or_404(Post, pk=post_id)
	return render(request, 'review/detail.html',{'post':post})