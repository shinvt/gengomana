from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from account.models import User, Teacher, Student

class Language(models.Model):
    language = models.CharField(max_length=30)

    def __str__(self):
        return self.name

CLASSROOM_STATE = (
    (0, 'Waiting Confirmation by teacher'),
    (1, 'Confirmed by teacher'),
    (2, 'Waiting Confirmation by student'),
    (3, 'Confirmed by student'),
)

class ClassRoom(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE, related_name='classroom_student')
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE, related_name='classroom_teacher')
    classroomtime_at = models.DateTimeField(null=True)
    state = models.IntegerField(choices=CLASSROOM_STATE,default=0)
