from rest_framework import serializers
from .models import Student, Subject, Status, PresenceStatus

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class PresenceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresenceStatus
        fields = '__all__'