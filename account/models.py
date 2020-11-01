from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField

class UserManager(UserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(_('username'), max_length=150, blank=True, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(_('email'), unique=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    class Types(models.TextChoices):
        STUDENT = "STUDENT", "Student"
        TEACHER = "TEACHER", "Teacher"

    base_type = Types.STUDENT

    # What type of user are we?
    type = models.CharField(
        _("Type"), max_length=50, choices=Types.choices, default=base_type
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["email"]

    def save(self, *args, **kwargs):
        # if not self.id:
        #     self.type = self.base_type
        return super().save(*args, **kwargs)


class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.STUDENT)

class TeacherManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.TEACHER)

# class Student(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE,parent_link=True,related_name='student',primary_key=True)
#
# class Teacher(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE,parent_link=True,related_name='teacher',primary_key=True)
#     language = ArrayField(models.CharField(max_length=30), blank=True)

class StudentExtend(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,parent_link=True,related_name='student')

class Student(User):
    is_student = True
    base_type = User.Types.STUDENT
    objects = StudentManager()

    @property
    def extendInfo(self):
        return self.studentextend

    # @property
    # def is_student(self):
    #     return self._is_student

    class Meta:
        proxy = True


class TeacherExtend(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,parent_link=True,related_name='teacher')
    language = ArrayField(models.CharField(max_length=30), blank=True)

class Teacher(User):
    is_teacher = True
    base_type = User.Types.TEACHER
    objects = TeacherManager()

    @property
    def extendInfo(self):
        return self.teacherextend

    # @property
    # def is_teacher(self):
    #     return self._is_teacher

    class Meta:
        proxy = True
