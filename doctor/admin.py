from django.contrib import admin

# Register your models here.
from doctor.models import Doctor, Department


class DepartmentAdmin(admin.ModelAdmin):
    pass
class DoctorAdmin(admin.ModelAdmin):
    search_fields = ('f_name', 'l_name', 'department',
                     )
    list_display = ['department', 'profession', 'f_name', 'l_name','address',
                    'tel']
    ordering = ('l_name', 'f_name', 'department', 'profession')
    fields = None



admin.site.register(Department, DepartmentAdmin)
admin.site.register(Doctor, DoctorAdmin)