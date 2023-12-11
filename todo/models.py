from django.db import models

# Create your models here.
class Todo(models.Model):
	title = models.CharField(max_length=100, blank=False, null=False)
	description = models.CharField(max_length=100, blank=False, null=False)
	completed = models.BooleanField(default=False)