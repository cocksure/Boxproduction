from django.urls import path
from django.contrib.auth.views import LoginView
# from .forms import UserLoginForm
from .views import main_view

urlpatterns = [
    path('', main_view, name='main-view'),
   ]