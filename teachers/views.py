from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.response import Response
from .serializers import *


class GetCoursesView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class GetCoursesDetailView(GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(serializer.data)


class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class RegisterCourseView(GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = RegisterCourseSerializer
    lookup_field = 'id'

    def get_student(self, student_id: int):
        if Student.objects.filter(id=student_id).exists():
            return Student.objects.get(id=student_id)
        raise ValueError

    @swagger_auto_schema(request_body=RegisterCourseSerializer)
    def post(self, request, *args, **kwargs):
        course = self.get_object()
        student = self.get_student(student_id=request.data.get('student_id'))
        if course in student.courses.all():
            return Response({'message': 'already signed'})
        student.courses.set([course])
        student.save()
        return Response({'message': 'ok'})


class TeacherListView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherListSerializer


class FinallyCourseTimeView(GenericAPIView):
    queryset = Course.objects.all()
    lookup_field = 'id'

    def post(self, request, *args, **kwargs):
        course: Course = self.get_object()
        print(course.total_count, course.time.all(), )
        return Response({'message': 'ok'})
