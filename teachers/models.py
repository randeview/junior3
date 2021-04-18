from django.db import models

from . import DayOfWeek
from django.utils.translation import gettext_lazy as _


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True


class DayOfWeek(models.Model):
    day_of_week = models.CharField('День недели', max_length=64,
                                   choices=DayOfWeek.choices)

    class Meta:
        verbose_name = 'День недели'

    def __str__(self):
        return self.day_of_week


class ScheduledTime(models.Model):
    day_of_week = models.ManyToManyField(DayOfWeek)
    start_hour = models.CharField(
        max_length=24 * 4,
        verbose_name=_('Start Hour(s)'),
    )
    start_minute = models.CharField(
        max_length=60 * 4,
        verbose_name=_('Start Minute(s)'),
    )
    end_hour = models.CharField(
        max_length=24 * 4,
        verbose_name=_('End Hour(s)'),
    )
    end_minute = models.CharField(
        max_length=60 * 4,
        verbose_name=_('End Minute(s)'),
    )

    class Meta:
        verbose_name = 'Время'
        verbose_name_plural = 'Время'

    def __str__(self):
        return f'{self.start_hour}:{self.start_minute},{self.end_hour}:{self.end_minute}'


class Teacher(TimestampMixin):
    full_name = models.CharField('ФИО', max_length=500)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Преподователь'
        verbose_name_plural = 'Преподователи'


class CourseTimeTeacher(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='course_time')
    scheduled_time = models.ForeignKey(ScheduledTime, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Время урока'

    def __str__(self):
        return f'{self.teacher} {self.scheduled_time}'


class Course(TimestampMixin):
    title = models.CharField('Название Курса', max_length=500)
    total_count = models.IntegerField('Количество уроков', default=0)
    time = models.ManyToManyField(CourseTimeTeacher, related_name='course_time_teacher')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return f'{self.title}'


class Student(TimestampMixin):
    name = models.CharField('ФИО Студента', max_length=500)
    courses = models.ManyToManyField(Course, related_name='students', blank=True)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return self.name


