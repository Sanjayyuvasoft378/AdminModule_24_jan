from django.contrib import admin
from django.urls import path,include

from adminapp.views import *
from .stripe import *
from adminapp import views,stripe


urlpatterns = [
    path('home/', stripe.HomeView, name='home'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/',views.logout,name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', stripe.home, name='homes'),
    path('create-checkout-session/', stripe.create_checkout_session, name='checkout'),
    path('success', stripe.success,name='success'),
    path('cancel.html/', stripe.cancel,name='cancel'),
    
    
    # path('category/', CategoryView.as_view(), name='category'),
    # path('stripe_data/',stripe.stripe_data,name='stripe_data'),
    
    
    path('plan/',PlanAPI.as_view(),name='plan'),
    path('PaymentView/',PaymentView,name='PaymentView'),
    path('create-checkout-session1/', views.create_checkout_session1, name='checkout1'),
    
    
    
    

]