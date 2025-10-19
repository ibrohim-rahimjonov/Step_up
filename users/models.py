from django.db import models
import uuid
from online_school import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')

        return self.create_user(email, username, password, **extra_fields)

class  User(AbstractBaseUser,PermissionsMixin):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    full_name = models.CharField(max_length = 50)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100,  blank=True,null=True)
    username = models.CharField(max_length=10, unique=True)
    password = models.TextField()
    role = models.CharField(
        max_length=20,
        choices=[
            ('admin','Admin'),
            ('teacher','Teacher'),
            ('student','Student'),

        ])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()  # connect the custom manager

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    

    def __str__(self):
        return f"{self.full_name}({self.role})"
    
class Group_enrollments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    group_name = models.CharField(max_length=100)
    # reference user model via settings to avoid import/circular problems
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_teaching_groups',
        limit_choices_to={'role': 'teacher'}
    )
    students = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='student_groups',
        limit_choices_to={'role': 'student'}
    )
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.group_name} - {self.teacher}"