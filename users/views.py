from django.shortcuts import render
from rest_framework import viewsets 
from .models import User
from .serializers import UserSerializers

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers