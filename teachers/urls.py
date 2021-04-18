from django.urls import path
from .views import *

urlpatterns = [
    path('course-list/', GetCoursesView.as_view(), name='course-list'),
    path('student-list/', StudentListView.as_view(), name='student-list'),
    path('course-detail/<int:id>/', GetCoursesDetailView.as_view(), name='course-detail'),
    path('course-register/<int:id>/', RegisterCourseView.as_view()),
    path('teacher-list/', TeacherListView.as_view()),
    path('course-suitable-time/<int:id>/', FinallyCourseTimeView.as_view())
]
