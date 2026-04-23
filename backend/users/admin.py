from django.contrib import admin
from .models import User,Permission, Role
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role' ,'is_staff', 'is_active')

    list_filter = ('is_staff', 'is_active','role')
    search_fields = ('username', 'email')
    ordering = ('id',)


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ( 'name','code', 'is_active')

    list_filter = ( 'is_active',)
    search_fields = ('name','code',)
    ordering = ('name',)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'is_active')

    list_filter = ('is_active',)
    search_fields = ('name',)
    ordering = ('name',)