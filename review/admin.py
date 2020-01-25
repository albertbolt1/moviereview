from django.contrib import admin

# Register your models here.
from .models import Post,Bigreview

admin.site.register(Post)
admin.site.register(Bigreview)
