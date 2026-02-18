from django.db import models
from django.conf import settings



# Create your models here.
User = settings.AUTH_USER_MODEL


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=50, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff_id
