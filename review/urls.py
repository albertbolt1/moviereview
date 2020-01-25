from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'review'
urlpatterns=[
	path('', views.home, name='home'),
	url(r'^(?P<post_id>[0-9]+)/$', views.bigreview, name='review1'),
]