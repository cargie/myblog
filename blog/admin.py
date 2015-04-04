from django.contrib import admin
from .models import Category, Article

# Register your models here.


# class CategoryInline(admin.S)
#     pass

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['created']
    # fieldsets = [
    #     ('Content',               {'fields': ['title', 'body', 'writer', 'slug', 'tags']}),
    #     ('Date Information', {'fields': ['created', 'modified'], 'classes': ['collapse']}),
    # ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)