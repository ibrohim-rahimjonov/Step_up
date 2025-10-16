import uuid
from django.db import models
from users.models import User

# Create your models here.
class Group(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=50,unique=True)
    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='group_teaching_groups',
        limit_choices_to={'role':'teacher'}
    )
    
    def __str__(self):
     return self.name

