from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from UserServices.models import Users


class SignupAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        profile_pic = request.data.get('profile_pic')

        if username is None or password is None:
            return Response({"error": "Username , password and email are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        user = Users.objects.create_user(username=username, email=email, password=password , profile_pic=profile_pic)
        user.save()
        refresh = RefreshToken.for_user(user)
        # here i am adding custom data whcih can be decodeed with access token
        access = refresh.access_token
        access['username'] = user.username
        access['email'] = user.email
        access['profile_pic'] = user.profile_pic.url if user.profile_pic else None

        return Response({'refresh': str(refresh), 'access': str(access),"message": "User created successfully."}, status=status.HTTP_201_CREATED)
    
       
class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(request, username=username, password=password)

        if user: 
            refresh = RefreshToken.for_user(user)
            # here i am adding custom data whcih can be decodeed with access token
            access = refresh.access_token
            access['username'] = user.username
            access['email'] = user.email
            access['profile_pic'] = user.profile_pic.url if user.profile_pic else None
            
            return Response({ 
                "refresh": str(refresh),
                "access": str(access),
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid username or password."}, status=status.HTTP_401_UNAUTHORIZED)


    def get(self, request):
        return Response({"message": "Please use post method to login"})