from django.db import models
from django.contrib.auth.models import  AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='email',
                              max_length=255, unique=True)
    
class Plan(models.Model):
    planId = models.CharField(max_length=20, unique=True)    
    planName = models.CharField(max_length=100,unique=True)
    price = models.IntegerField()
    
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
