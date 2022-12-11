from django.shortcuts import render
from api.serializers import *
from api.models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.http import Http404
# Create your views here.

class SignUpUserView(APIView):
    '''This api is use for signup email,name,phone_number and password'''
    def post(self,requst):
        serializer = SignUpUserSerializers(data=requst.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.data['password'])
            user.save()
            return Response({
                'status':"success",'data':serializer.data,
                'message':"account has been created successfully",
            },status=status.HTTP_201_CREATED)
        else:
            return Response({'status':serializer.errors})


class LoginUserView(APIView):
    '''This api is use for login with email and password'''
    def post(self,request):
        serializer = LoginUserSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email, password=password)

            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({'status':"success",'refresh':str(refresh),"access":str(refresh.access_token),
                },status=status.HTTP_200_OK)

            else:
                return Response({'status':serializer.errors,"messages":"invalid credential"})

class GetAllUser(APIView):
    '''This api is use to get all user'''
    def get(self,request):
        data = User.objects.all()
        serializer = UserSerializer(data,many=True)

        return Response({'status':"success","data":serializer.data})


class TaskCreate(APIView):
    '''This api is use to create Task task_name,priority and description'''
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self,request):
        user = request.user
        task_name = request.data.get('task_name',None)
        priority = request.data.get('priority',None)
        description = request.data.get('description',None)

        data ={
            "student_name":user.name,
            "email":user.email
        }
        if task_name:
            try:
                task = Task.objects.get(task_name=task_name,user=user)
                task.task_name = task_name
                task.priority =priority
                task.description = description
                task.save()
            except Exception as e:
                print(e)
                task_obj = Task.objects.create(task_name=task_name,priority=priority,description=description,user=user)
                task_obj.save()
            return Response({
                "status":"success",
                "student_info":data,
                "message":"task created successfully"
            },status=status.HTTP_201_CREATED)

class ShowAllTask(APIView):
    '''This api is use List all task'''

    permission_classes = [IsAuthenticated]

    def get(self,request):
        
        task = Task.objects.all()
        serializer = TaskSerializer(task,many=True)
        return Response({
            "status":"success",
            "task":serializer.data,
        }) 

class TaskUpdateDelete(APIView):
    '''This api use for  Retrieve, update or delete a task instance'''
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_object(self, pk):
        try:
            task = Task.objects.get(pk=pk)
            return task
        except Task.DoesNotExist:
            raise Http404
    def get(self,request,pk,format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response({"status":"success","data":serializer.data})
    
    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer =  TaskSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","update_data":serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response({"status":"success","message":"task deleted successfully"},status=status.HTTP_204_NO_CONTENT)

