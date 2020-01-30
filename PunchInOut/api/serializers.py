from django.conf.urls import url, include
from .models import  Employee, EmployeeAttendance
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['emp_id', 'name', 'email']

class EmployeeAttendanceSerializer(serializers.HyperlinkedModelSerializer):
    emp_id = serializers.CharField(source="emp.emp_id", read_only=True)
    class Meta:
        model = EmployeeAttendance
        fields = ['emp_id', 'start_date_time', 'end_date_time']