from django.contrib import admin
from .models import Group_enrollments

@admin.register(Group_enrollments)
class GroupEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'group', 'enrollment_date')
    list_filter = ('group', 'enrollment_date')
    search_fields = ('student__full_name', 'group__name')
