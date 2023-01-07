from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
# Register your models here.

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','email','username','password']

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['planId','planName','price']
    
@admin.register(CustomerModel)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['username','email','password','confirm_password','address']

# @admin.register(CustomUser)
# class Useradmin(admin.ModelAdmin):
#     list_display = ['username','email','password','confirm_password']

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['id','categoryName','description','categoryImage']
