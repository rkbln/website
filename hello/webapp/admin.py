from django.contrib import admin
from .models import Article
# Register your models here.



class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_filter = ['author']
    search_fields = ['title', 'body']
    fields = ['title', 'author', 'body', 'created_at', 'updated_at']
    exclude = ['id']
    readonly_fields = ['created_at', 'updated_at']

admin.site.register(Article, ArticleAdmin)
