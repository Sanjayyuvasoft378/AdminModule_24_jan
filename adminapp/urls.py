from django.contrib import admin
from django.urls import path,include

from adminapp.views import *
from adminapp import views,stripe


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',views.logout,name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('home/', views.HomeView, name='home'),
    # path('category/', CategoryView.as_view(), name='category'),
    # path('stripe_data/',stripe.stripe_data,name='stripe_data'),
    path('plan/',PlanAPI.as_view(),name='plan'),
    
    
    
    
    path('', views.home, name='homes'),
    path('create-checkout-session/', views.create_checkout_session, name='checkout'),
    path('success/', views.success,name='success'),
    path('cancel.html/', views.cancel,name='cancel'),

]