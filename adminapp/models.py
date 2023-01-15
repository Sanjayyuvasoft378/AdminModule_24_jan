from django.db import models
import stripe
from django.conf import settings
from django.db.models.signals import post_save
from datetime import datetime
from django.core import validators
from django.contrib.auth.models import  AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='email',
                              max_length=255,null=True,blank=True)

    customer_stripe_id = models.CharField(
        max_length = 50,
        null = True, blank = True
    )

    name = models.CharField(max_length=20,
        blank = True,
        null = True
    )

    def __str__(self):
        return self.customer_stripe_id


class Product(models.Model):
    # id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=70,null=True,blank=True)
    price = models.FloatField(null=True,blank=True)    
    description = models.TextField(max_length=800,verbose_name='Description',null=True,blank=True)





class Subscriber(models.Model):
    subscription_id = models.CharField(max_length=20,null=True,blank=True)
    name = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)


class Payment(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
    subscription_id = models.ForeignKey(Subscriber,on_delete=models.CASCADE,null=True,blank=True)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='pro_name',null=True,blank=True)
    amount_subtotal = models.CharField(max_length = 500,null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    payment_status = models.CharField(max_length = 25,null= True, blank = True)







MEMBERSHIP_CHOICES = (
    ('Standard', 'std'),
    ('Premium', 'pre'),
    ('Free', 'free')
)


class Membership(models.Model):
    slug = models.SlugField()
    membership_type = models.CharField(choices=MEMBERSHIP_CHOICES,
                                       default='Free',max_length=30)
    price = models.IntegerField(default=15)
    stripe_plan_id = models.CharField(max_length=40)

    def __str__(self):
        return self.membership_type


class UserMembership(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=40)
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username


def post_save_usermembership_create(sender, instance, created, *args, **kwargs):
    user_membership, created = UserMembership.objects.get_or_create(user=instance)


    if user_membership.stripe_customer_id is None or user_membership.stripe_customer_id == '':
        new_customer_id = stripe.Customer.create(email=instance.email)
        # free_membership = Membership.objects.get(membership_type='Stanard')
        user_membership.stripe_customer_id = new_customer_id['id']
        # user_membership.membership = free_membership
        user_membership.save()


post_save.connect(post_save_usermembership_create,sender=settings.AUTH_USER_MODEL)


class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=40)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_membership.user.username

    @property
    def get_created_date(self):
        subscription = stripe.Subscription.retrieve(self.stripe_subscription_id)
        return datetime.fromtimestamp(subscription.created)









# class Plan(models.Model):
#     planId = models.CharField(max_length=20, unique=True)    
#     planName = models.CharField(max_length=100,unique=True)
#     price = models.IntegerField()
    
# class CustomerModel(models.Model):
#     username = models.CharField(max_length=220)
#     email = models.EmailField(max_length=255,unique=True)
#     address = models.TextField(max_length=300)
#     password = models.CharField(max_length=15)
#     confirm_password = models.CharField(max_length=15)
#     def __str__(self):
#         return self.username

    
    

    
 
    # name = models.CharField(max_length=250)
    # tc = models.BooleanField()
    # is_active = models.BooleanField(default=True)
    # is_admin = models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)


    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['name', 'tc']

    # def __str__(self):
    #     return self.email

    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin
