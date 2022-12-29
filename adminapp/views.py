from django.shortcuts import render, redirect
from .models import *
from .serializers import *
from rest_framework.views import APIView
from django.http import JsonResponse
from django.contrib.auth import authenticate

# Create your views here.

def signup(request):
    return render(request, 'app/signup.html')

def login(request):
    return render(request,'app/login.html')

def home(request):
    return render(request,'app/home.html')

class UserRegistrationAPI(APIView):
    def post(self, request):
        try:
            Serializer = UserRegistrationSerialzier(data = request.data)
            if Serializer.is_valid():
                Serializer.save()
                return redirect('/adminapp/signin/')
            else:
                return redirect('/adminapp/signup/')
        except Exception as e:
            return redirect('/adminapp/signup/')

class LoginAPI(APIView):
    def post(self, request, format=None):
        try:
            Serializer = LoginSerializer(data = request.data)
            if Serializer.is_valid():
                email = request.data.get('email')
                password = request.data.get('password')
                user = authenticate(email=email, password=password)
                if user is not None:
                    return JsonResponse({"msg":"Login successfully"},safe=False)
                else:
                    return JsonResponse({"msg":"incorrect user"},safe=False)
            return JsonResponse({"msg":"invalid data"})
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False)
            
