from django.contrib.auth import views as auth_views
from django.views import generic
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
import json
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import LoginForm, RegisterForm
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

YOUR_DOMAIN = 'http://127.0.0.1:8000'

class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'app/signup.html'
    success_url = reverse_lazy('login')

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'app/login.html'
    
def logout(request):
    request.session.clear()
    return redirect('login')

# @login_required
# def HomeView(request):
#     data= []
#     product_data = stripe.Product.list().data
#     for i in product_data:
#         print("ss",i)
#         price_data = stripe.Price.retrieve(id = i.get("default_price"))
#         data.append({"name":i.get("name"), "price_amount":str(price_data.get("unit_amount"))[:2], "currency":price_data.get("currency"),"id":i.get("id"),})
#         print(data,"assssssssssss")
#     return render(request,'app/home.html',{"data":data})



@csrf_exempt
def create_checkout_session1(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_PRIVATE_KEY
        try:
            product = stripe.Product.list().data
            for i in product:   
                stripe.Customer.create(
                description="My First Test Customer (created for API docs at https://www.stripe.com/docs/api)",
                )
                price_data = stripe.Price.retrieve(id = i.get("default_price"))
                price_amount =str(price_data.get("unit_amount"))        
                print("&&&&&&&&&&&&",i.name)
                checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[{
                    'price_data': {
                    'currency': 'inr',
                    'product_data': {
                    'name': i.name,
                    },
                    'unit_amount': price_amount,
                    },
                    'quantity': 1,
                    }]
                )
                # return JsonResponse({'sessionId': checkout_session['id']})
                return render(request,'checkout.html')
            return JsonResponse({"msg":"error"})
        except Exception as e:
            return JsonResponse({'error': str(e)})
        
        



class PlanAPI(APIView):
    def post(self, request):
        form = PlanForm(data=request.data)
        if form.is_valid():
            form.save()
            return render(request, 'checkout.html',{"form":form})
        else:
            return Response({"msg":"sss "})












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




# @login_required
# def HomeView(request):
#     data= []
#     product_data = stripe.Product.list().data
#     for i in product_data:
#         print("ss",i)
#         price_data = stripe.Price.retrieve(id = i.get("default_price"))
#         import pdb;pdb.set_trace()
#         data.append({"name":i.get("name"), "price_amount":str(price_data.get("unit_amount"))[:2], "currency":price_data.get("currency"),"id":i.get("id"),})
#         print(data,"assssssssssss")
#     return render(request,'app/home.html',{"data":data})
