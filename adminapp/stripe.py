import stripe
from AdminModule import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
stripe.api_key = settings.STRIPE_PRIVATE_KEY
@login_required
def HomeView(request):
    data= []
    product_data = stripe.Product.list().data
    for i in product_data:
        print("ss",i)
        price_data = stripe.Price.retrieve(id = i.get("default_price"))
        data.append({"name":i.get("name"), "price_amount":str(price_data.get("unit_amount"))[:2], "currency":price_data.get("currency"),"id":i.get("id"),})
    return render(request,'app/home.html',{"data":data})
