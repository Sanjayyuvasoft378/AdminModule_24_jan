import stripe
from django.http import HttpResponse
from AdminModule import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from django.contrib import messages
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
        price_data = [x for x in price.data if x.product == i.id][0]
        price_ = float(price_data.unit_amount / 100)
        obj,_ = Product.objects.get_or_create(name=i.name)
        obj.price = price_
        obj.active = i.active
        obj.save()
        data.append({"name":i.get("name"), "price_amount":price_,"price_id":i.get("default_price"),"id":i.get("id"),})
        
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
        price_data = [x for x in price.data if x.product == i.id][0]
        price_ = int(price_data.unit_amount / 100)
        print(price_)
        # user_id = i.id
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
        stripe.api_key = 'sk_test_51LzfBbSAZLmnjHWeDGXSx3IQ67IAE0lYXHG0LUCcYg6kfb8PwaU9L039v68KBMQ20rezh3bphfrVuI1EjBtfdzmd00Zqo5WfNB'
        customer = stripe.Customer.create(
            email = request.user.email,
            source = request.POST.get('stripeToken')
        )
        
    return JsonResponse({'id': session.id,'customer':customer})




def user_membership(request):
    user_membership_qs = UserMembership.objects.filter(user=request.user)
    if user_membership_qs.exists():
        return user_membership_qs.first()
    return None


def user_subscription(request):
    user_subscription_qs = Subscription.objects.filter(
        user_membership=user_membership(request))
    if user_subscription_qs.exists():
        user_subscription = user_subscription_qs.first()
        return user_subscription
    return None


def selected_membership(request):
    membership_type = request.session['selected_membership_type']
    selected_membership_qs = Membership.objects.filter(
        membership_type=membership_type)
    if selected_membership_qs.exists():
        return selected_membership_qs.first()
    return None





@login_required
def PaymentView(request):
    try:
        selected_membership = selected_membership(request)
    except:
        return redirect(reverse("adminapp:login"))
    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == "POST":
        try:
            token = request.POST['stripeToken']
            user_membership = user_membership(request)

            customer = stripe.Customer.retrieve(user_membership.stripe_customer_id)
            customer.source = token 
            customer.save()

            subscription = stripe.Subscription.create(
                customer=user_membership.stripe_customer_id,
                items=[
                    { "plan": selected_membership.stripe_plan_id },
                ]
            )
            return redirect(reverse('adminapp:update-transactions',
                                    kwargs={
                                        'subscription_id': subscription.id
                                    }))
        except:
            messages.info(request, "An error has occurred, investigate it in the console")

    context = {
        'publishKey': publishKey,
        'selected_membership': selected_membership
    }

    return render(request, "/membership_payment.html", context)
