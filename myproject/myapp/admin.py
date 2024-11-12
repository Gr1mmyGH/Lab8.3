# myapp/admin.py

from django.contrib import admin
from .models import Students, Subjects, Exams

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'lastname', 'name', 'telephone')  # Поля для отображения
    search_fields = ('lastname', 'name')  # Поля для поиска

class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'hours', 'semesters')
    search_fields = ('name',)

class ExamsAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'student', 'subject', 'grade')
    list_filter = ('date', 'grade')  # Фильтрация по дате и оценке

# Регистрируем модели с дополнительными настройками
admin.site.register(Students, StudentsAdmin)
admin.site.register(Subjects, SubjectsAdmin)
admin.site.register(Exams, ExamsAdmin)
