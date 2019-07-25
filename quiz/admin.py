from django.contrib import admin

# Register your models here.
from quiz.models import User, Guest


@admin.register(User)
class UserAcmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Guest)
class GuestAcmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'score']