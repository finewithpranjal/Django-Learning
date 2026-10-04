from django.contrib import admin
from student.models import Profile, Result


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'email', 'city')


admin.site.register(Profile, ProfileAdmin)


@admin.register(Result) # we can also use this decorator function to register the model with the admin site
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'stu_class', 'marks')


# admin.site.register(Result, ResultAdmin)