from django.db import models

# Create your models here.
class ClassRoom(models.Model):
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=20)
    class_teacher = models.ForeignKey(
        'teachers.Teacher',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_classes"
    )

    def __str__(self):
        return f"{self.name} ({self.level})"


class Subject(models.Model):
    teacher = models.ForeignKey(
        'teachers.Teacher',
        on_delete=models.CASCADE,
        related_name="subjects"
    )
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} - {self.code}"


class Schedule(models.Model):
    class_room = models.ForeignKey(
        ClassRoom,
        on_delete=models.CASCADE,
        related_name="schedules"
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="schedules"
    )
    teacher = models.ForeignKey(
        'teachers.Teacher',
        on_delete=models.CASCADE,
        related_name="schedules"
    )

    DAY_CHOICES = (
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
    )

    day_of_week = models.CharField(max_length=3, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.class_room} - {self.subject} ({self.day_of_week})"
