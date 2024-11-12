from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students_list, name='students_list'),
    path('subjects/', views.subjects_list, name='subjects_list'),
    path('exams/', views.exams_list, name='exams_list'),
    path('lab8/', views.lab8_page, name='lab8_page'),
    path('students/<pk>/edit/', views.StudentUpdateView.as_view(), name='student_edit'),
    path('subjects/<pk>/edit/', views.SubjectUpdateView.as_view(), name='subject_edit'),
    path('exams/<pk>/edit/', views.ExamUpdateView.as_view(), name='exam_edit'),
]
