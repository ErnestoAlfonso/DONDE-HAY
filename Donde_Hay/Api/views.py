from django.shortcuts import render, HttpResponse
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
#from rest_framework.decorators import APIView
# Create your views here.
# class UserList(APIView):
#     def get(self, request):
#         if request.method == 'GET':
#             users = User.objects.all()
#             serializer = UserSerializer(users, many=True)

#         return Response(serializer.data)

# There is another thing named mixins that is "El hierro vivo"

@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
