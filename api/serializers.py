from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from api.models  import *
from rest_framework.serializers import SerializerMethodField

## define here serializers class

class SignUpUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'name',
            'phone_number',
            'password',
        )

class LoginUserSerializers(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128)
    
    class Meta:
        model = User
        fields = (
            'email','password',
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'email',
            'phone_number',
            'created_date',
            'updated_date',
        )



class TaskSerializer(serializers.ModelSerializer):
    student_name = SerializerMethodField()
    student_email = SerializerMethodField()
    class Meta:
        model = Task
        fields = (
            'id',
            'task_name',
            'priority',
            'description',
            'student_name',
            'student_email',
            'created_date',
            'updated_date',
            )

    def get_student_name(self,obj):
        data = obj.user.name
        return data
    def get_student_email(self,obj):
        data = obj.user.email
        return data
