import stripe
from django.http import HttpResponse
from AdminModule import settings
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

YOUR_DOMAIN = 'http://127.0.0.1:8000'
stripe.api_key = settings.STRIPE_PRIVATE_KEY
products = stripe.Product.list()
price = stripe.Price.list()

@login_required
def HomeView(request):
    data = []
    for i in products.data:
        print("2222222",i)
        price_data = [x for x in price.data if x.product == i.id][0]
        price_ = float(price_data.unit_amount / 100)
        print(price_)
        obj, _ = Product.objects.get_or_create(name=i.name)
        obj.price = price_
        obj.active = i.active
        obj.save()
        data.append({"name":i.get("name"), "price_amount":price_,"id":i.get("id"),})
        
    return render(request,'app/home.html',{"data":data})
    
#home view
def home(request):
 return render(request,'checkout.html')

#success view
def success(request):
 return render(request,'success.html')

 #cancel view
def cancel(request):
 return render(request,'cancel.html')

@csrf_exempt
def create_checkout_session(request):
    stripe.api_key = settings.STRIPE_PRIVATE_KEY
    for i in products.data:
        print("22222222222222222",i)
        price_data = [x for x in price.data if x.product == i.id][0]
        price_ = float(price_data.unit_amount / 100)
        print(price_)
        session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data': {
                'currency': 'inr',
                'product_data':
                    {
                    'name': i.name,
                    },
                    'unit_amount':100,
                },
                    'quantity': 1,
            }
                ],
        mode='payment',
        success_url=YOUR_DOMAIN + '/adminapp/success',
        cancel_url=YOUR_DOMAIN + '/adminapp/cancel',
        )
        order = Payment()
        # order.pro_name = Product.objects.get('name')
        # order.product = i.name
        order.stripe_payment_intent = session['payment_intent']
        # order.amount = int(price_)
        order.save()

        
    return JsonResponse({'id': session.id})

