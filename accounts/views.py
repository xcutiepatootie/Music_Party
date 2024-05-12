

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer

# Create your views here.
@api_view(['GET'])
def getUser(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createUser(request):
    print(request.data)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):
   
    def get_user(self, pk):
        try:
            student = User.objects.get(id=pk)
            return student
        except:
            return JsonResponse("Student Does Not Exist", safe=False)
        
    def get(self, request, pk=None):
        if pk:
            users = self.get_user(pk)
            serializer = UserSerializer(users,)
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
        
    def post(request):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        user_to_delete = User.objects.get(id=pk)
        user_to_delete.delete()
        return Response("User Successfully Deleted")

    def put(self, request, pk=None):
        user_to_update = User.objects.get(id=pk)
        serializer = UserSerializer(instance=user_to_update, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("User Successfully Updated", safe=False)
        return JsonResponse("Failed to Update Student")
