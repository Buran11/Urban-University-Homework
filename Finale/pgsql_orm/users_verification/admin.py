from django.contrib import admin  # type: ignore
from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password',
                    'data', 'time', 'is_verified',)
    list_filter = ('username', 'email', 'data', 'time', 'is_verified',)
    search_fields = ('username', 'email', 'data', 'time',)
    list_per_page = 200
    
