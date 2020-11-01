from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from account.models import User,Student,Teacher

class StudentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.type=User.Types.STUDENT
        user.is_student=True
        user.save()
        return user

class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.type=User.Types.TEACHER
        user.is_teacher=True
        user.save()
        return user
