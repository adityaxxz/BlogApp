from django.contrib import admin
from .models import Category, Post

# Register your models here.

admin.site.register(Category)
# admin.site.register(Post)

@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',)}