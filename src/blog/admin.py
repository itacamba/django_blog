from django.contrib import admin

# Register your models here.


#add the blog model into admin
from .models import BlogPost
admin.site.register(BlogPost)