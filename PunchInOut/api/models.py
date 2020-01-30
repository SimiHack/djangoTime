from django.db import models
from django.utils.timezone import datetime
import datetime

# Create your models here.

class Employee(models.Model):
    emp_id = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=25)
    def __str__(self):
        return self.emp_id

class EmployeeAttendance(models.Model):
    emp = models.ForeignKey(
        Employee,
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.PROTECT,
    )
    start_date_time = models.DateTimeField(default=datetime.datetime.now, blank=True)
    end_date_time = models.DateTimeField(default=datetime.datetime.now, blank=True)
    
