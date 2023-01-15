from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
# Register your models here.

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','email','username','password']



@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user_id','subscription_id','created_at','product_name','amount_subtotal','payment_status']


# @admin.register(CustomUser)
# class Useradmin(admin.ModelAdmin):
#     list_display = ['username','email','password','confirm_password']



# @admin.register(Plan)
# class PlanAdmin(admin.ModelAdmin):
#     list_display = ['planId','planName','price']
    
# @admin.register(CustomerModel)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ['username','email','password','confirm_password','address']


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['id','categoryName','description','categoryImage']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price']
    
@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ['slug','membership_type','price','stripe_plan_id']
    
@admin.register(UserMembership)
class UserMembershipAdmin(admin.ModelAdmin):
    list_display = ['user','stripe_customer_id','membership']
    
    
@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user_membership','stripe_subscription_id','active']
