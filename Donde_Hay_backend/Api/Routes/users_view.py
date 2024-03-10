from ..Models.models import User
from ..Schemas.serializers import UserSerializer, UserSearchSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action



class UserMethods(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    #Actions with User Table
    @action(detail=False)
    def searchBy(self, request : Request):
        request_serializer = UserSearchSerializer(data=request.query_params)
        searchMethods = {
            "username" : self.searchByUsername,
            "email" : self.searchByEmail,
            "phone" : self.searchByPhoneNumber 
        }
        if request_serializer.is_valid():
            user = searchMethods[request_serializer.data["field"]](request_serializer.data["value"])
            if user:
                user_schema = self.get_serializer(user)
                return Response(user_schema.data, status=status.HTTP_200_OK)
            else:
                return Response({}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    @action(detail=False)
    def login(self, request):
        #TODO: implement
        pass

    @action(detail=True)
    def forgot_password(self, request, pk=None):
        #TODO: implement
        pass

    #Utils
    def searchByEmail(self, email):
        return self.queryset.filter(email=email).first()
    
    def searchByPhoneNumber(self, phone):
        return self.queryset.filter(phone=phone).first()
    
    def searchByUsername(self, username):
        return self.queryset.filter(username=username).first()







#from rest_framework.decorators import APIView
# Create your views here.
# class UserList(APIView):
#     def get(self, request):
#         if request.method == 'GET':
#             users = User.objects.all()
#             serializer = UserSerializer(users, many=True)

#         return Response(serializer.data)

# There is another thing named mixins that is "El hierro vivo"


