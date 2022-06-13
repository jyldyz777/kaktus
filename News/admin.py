from django.contrib import admin

from News.models import Category, News, Comment

admin.site.register(Category)
admin.site.register(News)
admin.site.register(Comment)
