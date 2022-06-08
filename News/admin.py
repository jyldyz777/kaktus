from django.contrib import admin

# Register your models here.
from News.models import Category, News, Comment

admin.site.register(Category)
admin.site.register(News)
admin.site.register(Comment)