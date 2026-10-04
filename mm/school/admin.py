from django.contrib import admin
from school.models import *
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display  = ['id', 'name', 'roll', 'city', 'marks', 'pass_date', 'addmission_date']
