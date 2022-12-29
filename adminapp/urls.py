from django.contrib import admin
from django.urls import path

from adminapp.views import LoginView, RegisterView, HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('home/', HomeView.as_view(), name='home'),
]