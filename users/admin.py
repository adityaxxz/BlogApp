from django.contrib import admin
from .models import NewUser
# Register your models here.


@admin.register(NewUser)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('email', 'id', 'user_name', 'first_name', 'is_active', 'is_staff', 'start_date')
    list_filter = ('email', 'user_name', 'is_staff')
    search_fields = ('email', 'user_name', 'first_name')
    ordering = ('email',)
