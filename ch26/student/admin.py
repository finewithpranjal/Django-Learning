from django.contrib import admin
from student.models import user
# Register your models here.

@admin.register(user)
class userAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'password', 'email']