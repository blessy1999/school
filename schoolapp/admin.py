from django.contrib import admin
from .models import Department,Course,Material
# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Department,DepartmentAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','department']
admin.site.register(Course,CourseAdmin)

class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name',]
admin.site.register(Material,MaterialAdmin)