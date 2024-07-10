from django.db import models

# Create your models here.

class Tasks(models.Model):
  """短期任务表"""

class longperiodtasks(models.Model):
  """长期任务表"""

class routinetasks(models.Model):
  """周期性任务表"""
  