from django.contrib import admin
from . import models

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ("created", "user", "text", "tbd")

admin.site.register(models.Task, TaskAdmin)
