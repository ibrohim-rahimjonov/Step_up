from django.contrib import admin
from .models import Group
from group_enrollments.models import Group_enrollments

class GroupEnrollmentInline(admin.TabularInline):
    model = Group_enrollments
    extra = 1

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')
    inlines = [GroupEnrollmentInline]
