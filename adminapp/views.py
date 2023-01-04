
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import LoginForm, RegisterForm
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'app/login.html'


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'app/signup.html'
    success_url = reverse_lazy('login')
    
def logout(request):
    request.session.clear()
    return redirect('login')

class PlanAPI(APIView):
    def post(self, request):
        form = PlanForm(data=request.data)
        if form.is_valid():
            form.save()
            return render(request, 'app/plan.html',{"form":form})
        else:
            return render(request,'app/home.html')














# class HomeView(APIView):
#     def HomeView(request):
#         # return Response({"message":"Login successfully"})
#         return render(request,'app/home.html')



# class CategoryView(APIView):
#     def get(self, request):
#         try:
#             get_data = Category.objects.all()
#             form = CategoryForm(get_data)
#             return Response(form.data)
#         except Exception as e:
#             return Response({"msg":"Internal server error{}".format(e)})

#     def post(self, request):
#         try:
#             form = CategoryForm(data=request.data)
#             if form.is_valid():
#                 form.save()
#                 return Response({"msg":"data added successfully"})
#             else:
#                 return Response({"msg":"Invalid Input Data"})
#         except Exception as e:
#             return Response({"msg":"Internal server error {}".format(e)})
        
#     def delete(self, request, pk):
#         try:
#             pk = Category.objects.get(pk)
#             form = CategoryForm(pk=pk)
#             form.delete()
#             return Response({"msg":"data deleted successfully"})
#         except Exception as e:
#             return Response({"msg":"Internal server error {}".format(e)})