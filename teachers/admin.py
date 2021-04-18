from django.contrib import admin
from .models import *

admin.site.register(Teacher)
admin.site.register(ScheduledTime)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(CourseTimeTeacher)
admin.site.register(DayOfWeek)
