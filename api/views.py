from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
