from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def HomeView(request):
    free = {
    "planId":"free_012",
    "planName":'Free',
    "price":0,
    }
    premium = {
    "planId":"premium_123",
    "planName":"Premium",
    "price":"10$"
    }
    standard = {
    "planId":"standard_123",
    "planName":"Standard",
    "price":"20$"
    }
    return render(request,'app/home.html',{"get_data":free,"get_premium":premium,"get_standard":standard})

