"""bankmanagement URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('manager/', views.client_list, name='client_list'),
    path('manager/<int:admin_id>', views.client_form, name='client_insert'),
    path('manager/<int:admin_id>/clients/<int:client_id>', views.client_form, name='client_update'),
    path('manager/<int:admin_id>/clients/<int:client_id>/delete', views.client_delete, name='client_delete'),
    path('manager/<int:admin_id>/clients/<int:client_id>/list', views.account_list,  name='account_list'),
    path('manager/<int:admin_id>/clients/<int:client_id>/accounts', views.account_form,  name='add_account'),
]
