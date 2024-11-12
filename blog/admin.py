from django.contrib import admin
from .models import BlogCategory, BlogAuthor, BlogPost, PostComment

# Register your models here.


admin.site.register(BlogCategory)
admin.site.register(BlogAuthor)
admin.site.register(BlogPost)
admin.site.register(PostComment)