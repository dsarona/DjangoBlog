#from django.contrib import admin

from django.contrib import admin # <- this is already there.
from myblog.models import Post
from myblog.models import Category

admin.site.register(Post)


# and a new admin registration
admin.site.register(Category)
