from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class UserDetailsView(ListAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

class CustomerRegisterView(CreateAPIView): 
    queryset = User.objects.all() 
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class CustomerLoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request): 
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            user_serializer = UserSerializer(user)
            return Response({'refresh' : str(refresh),'access' : str(refresh.access_token),'user' : user_serializer.data})
        else:
            return Response({'detail' : 'Invalid credentials'}, 401)

class DashboardView(APIView):
    permission_classes = (IsAuthenticated,) 
    def get(self, request):     
        user = request.user
        user_serializer = UserSerializer(user)
        return Response({'message' : 'Welcome to the dashboard', 'user' : user_serializer.data}, 200)

