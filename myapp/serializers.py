from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['name', 'age', 'email']
        fields = '__all__' #Include all fields of the Student model in the serializer