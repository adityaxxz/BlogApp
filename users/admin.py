from django.contrib import admin
from .models import NewUser
# Register your models here.


@admin.register(NewUser)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('email', 'id', 'username', 'first_name', 'is_active', 'is_staff', 'start_date')
    list_filter = ('email', 'username', 'is_staff')
    search_fields = ('email', 'username', 'first_name')
    ordering = ('email',)
