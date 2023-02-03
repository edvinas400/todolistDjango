from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone


# Create your models here.
class Task(models.Model):
    created = models.DateTimeField("Created", auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.CharField("Name", max_length=200, help_text="Name/info of the task")
    tbd = models.DateTimeField("Until", null = True, blank=True)

    def is_overdue(self):
        now = timezone.now()
        return self.tbd and self.tbd < now

    def __str__(self):
        return f"{self.text}"

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ['tbd']