from django.urls import path
from adminapp import views
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('signin/',views.login,name='signin'),
    path('home/',views.home,name='home'),
    path('registration/',views.UserRegistrationAPI.as_view(),name='registraion'),
    path('login/',views.LoginAPI.as_view(),name='login'),
]
