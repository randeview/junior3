from rest_framework import serializers
from .models import *


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = DayOfWeek
        fields = ['day_of_week']


class ScheduleSerializer(serializers.ModelSerializer):
    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()
    day_of_week = DaySerializer(many=True)

    def get_start_time(self, instance: ScheduledTime):
        return f'{instance.start_hour}:{instance.start_minute}'

    def get_end_time(self, instance: ScheduledTime):
        return f'{instance.end_hour}:{instance.end_minute}'

    class Meta:
        model = ScheduledTime
        fields = ['day_of_week', 'start_time', 'end_time']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['full_name']


class TeacherTimeSerilizer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    scheduled_time = ScheduleSerializer()

    class Meta:
        model = CourseTimeTeacher
        fields = ['id', 'scheduled_time', 'teacher']


class CourseDetailSerializer(serializers.ModelSerializer):
    time = TeacherTimeSerilizer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'total_count', 'time']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title']


class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'courses']


class RegisterCourseSerializer(serializers.Serializer):
    student_id = serializers.IntegerField()


class TeacherListSerializer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField()

    def get_course(self, instance: Teacher):
        for course_time in instance.course_time.all():
            return CourseSerializer(course_time.course_time_teacher.all(), many=True).data

    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'course']
