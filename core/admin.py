from django.contrib import admin
from .models import BlogArticle
# Register your models here.
# admin.site.register(BlogArticle)
@admin.register(BlogArticle)
class BlogArticleModel(admin.ModelAdmin):
    list_filter=('title','description')
    list_display=('title','description')