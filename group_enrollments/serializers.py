from rest_framework import serializers
from .models import Group_enrollments

class Group_enrollmentsSerializir(serializers.ModelSerializer):
    class Meta:
        model = Group_enrollments
        fields = '__all__'