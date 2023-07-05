from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed
from .models import Aboutus, Faq, Home, Services, Teams,Terms,Privacy, Testimonials, Utilities
from .serializers import AboutSerializer, AllUserSerializer, FaqSerializer, HomeSerializer, PrivacySerializer, ServicesSerializer, TeamSerializer, TermsSerializer, TestimonialsSerializer, UserSerializer, UtilitiesSerializer
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
class FaqViews(viewsets.ModelViewSet):
    serializer_class = FaqSerializer
    queryset = Faq.objects.all()
class TermsViews(viewsets.ModelViewSet):
    serializer_class = TermsSerializer
    queryset = Terms.objects.all()
class PrivacyViews(viewsets.ModelViewSet):
    serializer_class = PrivacySerializer
    queryset = Privacy.objects.all()
class AboutViews(viewsets.ModelViewSet):
    serializer_class = AboutSerializer
    queryset = Aboutus.objects.all()

#dsd
class HomeViews(viewsets.ModelViewSet):
    serializer_class = HomeSerializer
    queryset = Home.objects.all()
class ServiceViews(viewsets.ModelViewSet):
    serializer_class = ServicesSerializer
    queryset = Services.objects.all()
class TestimonialsViews(viewsets.ModelViewSet):
    serializer_class = TestimonialsSerializer
    queryset = Testimonials.objects.all()
class TeamViews(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Teams.objects.all()
class UtilitiesViews(viewsets.ModelViewSet):
    serializer_class = UtilitiesSerializer
    queryset = Utilities.objects.all()

class RegisterUser(APIView):
    def post(self,requests):
        serializer = UserSerializer(data = requests.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({
            'status':403,
            "errors": serializer.errors,
            "message": "User data not valid"
            
            })
        serializer.save()
        user = User.objects.get(username= serializer.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({
            'status':200,
            "payload": serializer.data,
            'refresh': str(refresh),
            'access': str(refresh),
            "message": "You logged in successfully"
            
            })

class Userme(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AllUserSerializer
    def get_queryset(self):
        token = self.request.headers.get('Authorization').split()[1]
        payload = AccessToken(token).payload
        user_id = payload.get('user_id')
        return User.objects.filter(id=user_id)
    
