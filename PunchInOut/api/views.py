from .models import *
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

def time_view_set(request):
    
    if request.method == "GET":
        # emp_id = request.GET['Employee_emp_id']
        # if emp_id is not None:
            # detail = EmployeeAttendance.objects.filter(emp_id=emp_id)
            detail = EmployeeAttendance.objects.all()
            serializer = EmployeeAttendanceSerializer(detail, many=True)
            return JsonResponse(serializer.data, safe=False)