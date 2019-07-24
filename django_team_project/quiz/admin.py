from django.contrib import admin
from  .models import User, Guest
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code', 'p1', 'p2']


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'p1', 'p2']
