from django.contrib import admin
from student.models import *
class userAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'email']


admin.site.register(user, userAdmin)
