from django.db import models
from django.conf import settings




# Create your models here.
User = settings.AUTH_USER_MODEL


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reg_number = models.CharField(max_length=50, unique=True)
    class_assigned = models.ForeignKey(
        'academics.ClassRoom',
        on_delete=models.SET_NULL,
        null=True,
        related_name="students"
    )

    def __str__(self):
        return self.reg_number
