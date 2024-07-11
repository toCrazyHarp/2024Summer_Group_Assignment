from django.db import models

# Create your models here.

class Tasks(models.Model):
  """短期任务表"""
  title = models.CharField(max_length=100)
  start_time = models.DateTimeField()
  ischecked=models.BooleanField(default=False)

class longperiodtasks(models.Model):
  """长期任务表"""
  title = models.CharField(max_length=100)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  ischecked=models.BooleanField(default=False)


class routinetasks(models.Model):
  """周期性任务表"""
  title = models.CharField(max_length=100)
  mode = models.CharField(max_length=1)
  day = models.IntegerField
