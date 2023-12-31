from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RegisterSerializer
from .serializers import InstitutionRegisterSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from . models import User
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse


class RegisterVeiw(generics.GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        


        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token

 



        current_site = get_current_site(request).domain
        relativeLink =reverse('email-verify')

        
        absurl= 'http://'+str(current_site)+str(relativeLink)+'?token='+str(token)
        email_body = 'H' + user.Username+'Use the link below to verify your email \n'+ absurl,
        data={'email_body': email_body, 'subject': 'Verify your email address'}
        Util.send_email(data)

        return  Response(user_data, status=status.HTTP_201_CREATED)


 
class VerifyEmail(generics.GenericAPIView):
    def get(self):
        pass
 


class InstitutionRegisterVeiw(generics.GenericAPIView):

    serializer_class =InstitutionRegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data
        return  Response(user_data, status=status.HTTP_201_CREATED)

