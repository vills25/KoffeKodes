from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(generics.CreateAPIView): 
    queryset = User.objects.all() 
    permission_classes = (AllowAny,) # anyone can register, # this is a comma separated Tuple # we can also define This is in list[]
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request): 
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            user_serializer = UserSerializer(user)
            return Response({
                'refresh' : str(refresh),
                'access' : str(refresh.access_token),
                'user' : user_serializer.data
            })
        else:
            return Response({'detail' : 'Invaalid credentials'}, status = 401)

class DashboardView(APIView):
    permission_classes = (IsAuthenticated,) # to ensure that only authenticated users can access this Dashboard.
                       # (IsAuthenticatedOrReadOnly)	Auth users = full access, guests = read-only
    def get(self, request):     
        user = request.user
        user_serializer = UserSerializer(user)
        return Response({'message' : 'Welcome to the dashboard', 'user' : user_serializer.data}, 200)
    
