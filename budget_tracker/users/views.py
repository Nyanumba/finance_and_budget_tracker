from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated
from .models import Profile

class RegisterView(APIView):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, email=email, password=password)
        Profile.objects.create(user=user)
        refresh = RefreshToken.for_user(user)
        login(request, user)
        request.session['access_token'] = str(refresh.access_token)
        return redirect('dashboard')

class LoginView(APIView):
    def get(self, request):
        return render(request, 'login.html')  # Render login form for GET

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            request.session['access_token'] = str(refresh.access_token)
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        return Response({'user_id': request.user.id, 'preferred_currency': profile.preferred_currency})

    def put(self, request):
        profile = Profile.objects.get(user=request.user)
        profile.preferred_currency = request.data.get('preferred_currency', profile.preferred_currency)
        profile.save()
        return Response({'preferred_currency': profile.preferred_currency})

class ProfileFrontendView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        return render(request, 'profile.html', {'profile': profile})

    def post(self, request):
        profile = Profile.objects.get(user=request.user)
        profile.preferred_currency = request.data.get('preferred_currency', profile.preferred_currency)
        profile.save()
        return redirect('profile')