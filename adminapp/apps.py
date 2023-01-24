from django.apps import AppConfig


class AdminappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'adminapp'
    
    
    
    
    # normal user
#   sanjayyuvasoft378
#   Sanju1411


# superuser -- sanjay123
#   superuser   sanju1411


    # payment_method = stripe.PaymentMethod.attach(
    # "pm_1MRC6RSAZLmnjHWe0ikFDjzW",
    # customer="cus_NAraKmrnOIh9Xn",
    # )



    # subscription = stripe.Subscription.create(
    # customer="cus_NAraKmrnOIh9Xn", 
    # items=[
    #     {"price": "price_1MRXxcSAZLmnjHWebTjm4oJU"},
    # ],
    # )