from django.contrib import admin
from .models import ClassRoom, Subject, Schedule

# Register your models here.
admin.site.register(ClassRoom)
admin.site.register(Subject)
admin.site.register(Schedule)
