"""ReferralSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ReferralApp.views import register_user, user_details, user_referrals

urlpatterns = [
    path('api/register/', register_user, name='register_user'),
    path('api/user/details/', user_details, name='user_details'),
    path('api/user/referrals/', user_referrals, name='user_referrals'),
    # Other URL patterns for your Django app
]
