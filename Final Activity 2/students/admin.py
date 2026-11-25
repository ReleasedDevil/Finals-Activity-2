from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "last_name", "first_name", "course", "year_level", "section")
    search_fields = ("student_id", "first_name", "last_name", "course")
    list_filter = ("year_level", "section", "course")
