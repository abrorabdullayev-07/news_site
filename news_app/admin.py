from django.contrib import admin
from .models import Category, News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','category','status')
    prepopulated_fields = {'slug':['title',]}
    list_filter = ('status','category')
    search_fields = ('title', 'body')


admin.site.register(Category)
admin.site.register(News, NewsAdmin)