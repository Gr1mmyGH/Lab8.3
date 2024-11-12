# myapp/views.py

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import Students, Subjects, Exams

def students_list(request):
    students = Students.objects.all()  # Получаем все записи из модели Students
    return render(request, 'myapp/students_list.html', {'students': students})

def subjects_list(request):
    subjects = Subjects.objects.all()
    return render(request, 'myapp/subjects_list.html', {'subjects': subjects})

def exams_list(request):
    exams = Exams.objects.all()
    return render(request, 'myapp/exams_list.html', {'exams': exams})
def lab8_page(request):
    return render(request, 'myapp/lab8_page.html')

# Представление для редактирования записей в таблице Students
class StudentUpdateView(UpdateView):
    model = Students
    fields = ['lastname', 'name', 'surname', 'address', 'telephone', 'level', 'department', 'groupname', 'headman']
    template_name = 'myapp/student_form.html'
    success_url = reverse_lazy('students_list')

# Представление для редактирования записей в таблице Subjects
class SubjectUpdateView(UpdateView):
    model = Subjects
    fields = ['name', 'hours', 'semesters']
    template_name = 'myapp/subject_form.html'
    success_url = reverse_lazy('subjects_list')

# Представление для редактирования записей в таблице Exams
class ExamUpdateView(UpdateView):
    model = Exams
    fields = ['date', 'student', 'subject', 'grade']
    template_name = 'myapp/exam_form.html'
    success_url = reverse_lazy('exams_list')
