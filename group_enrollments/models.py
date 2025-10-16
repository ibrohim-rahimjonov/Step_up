import uuid
from django.db import models
from users.models import User
from groups.models import Group

# Create your models here.

class Group_enrollments(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='enrollments')
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='enrollments',
        limit_choices_to={'role':'student'}
    )
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.full_name} → {self.group.name}"