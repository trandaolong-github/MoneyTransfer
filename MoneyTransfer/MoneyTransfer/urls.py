"""MoneyTransfer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views

from TransferApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.transfer_home, name='transfer-home'),
    path('sign-up/', views.customer_sign_up, name='sign-up'),
    path('sign-in/', auth_views.LoginView.as_view(template_name='sign_in.html'), name='sign-in'),
    path('sign-out/', auth_views.LogoutView.as_view(next_page='/'), name='sign-out'),
    path('account-report/', views.account_report, name='account-report'),
    path('create-transaction/', views.create_transaction, name='create-transaction'),
]
