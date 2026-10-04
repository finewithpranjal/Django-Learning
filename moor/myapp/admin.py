from django.contrib import admin
from myapp.models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'city']


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['page_name']


@admin.register(like)
class likeAdmin(admin.ModelAdmin):
    list_display = ['likes'] 