
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy

from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import LoginForm, RegisterForm


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'app/login.html'


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'app/signup.html'
    success_url = reverse_lazy('login')

class HomeView(APIView):
    def get(self, request):
        return Response({"message":"Login successfully"})