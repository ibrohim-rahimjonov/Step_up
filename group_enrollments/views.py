from django.shortcuts import render
from rest_framework import viewsets
from group_enrollments.models import Group_enrollments
from .serializers import Group_enrollmentsSerializir

# Create your views here.
class Group_enrollmentsViewSet(viewsets.ModelViewSet):
    queryset = Group_enrollments.objects.all()
    serializer_class = Group_enrollmentsSerializir