"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from location import views

from rest_framework.authtoken import views
from equipments.api import EquipmentList, EquipmentDetail
from location.api import DivisionList, MasterList, SiteList, YardList, DivisionDetail, MasterDetail, SiteDetail, \
    YardDetail
from transactions.api import TransactionList, TransactionDetail
from user.api import DriverList, DriverDetail

urlpatterns = [
    path("admin/", admin.site.urls),
    path('location/', include('location.urls')),
    path('equipments/', include('equipments.urls')),
    path('transactions/', include('transactions.urls')),
    path('user/', include('user.urls')),
    path('api/equipment_list', EquipmentList.as_view(), name='equipment_list'),
    path('api/equipment_list/<int:equipment_id>', EquipmentDetail.as_view(), name='equipment_list'),
    path('api/division_list', DivisionList.as_view(), name='division_list'),
    path('api/division_list/<int:division_id>', DivisionDetail.as_view(), name='division_list'),
    path('api/master_list', MasterList.as_view(), name='master_list'),
    path('api/master_list/<int:id>', MasterDetail.as_view(), name='master_list'),
    path('api/site_list', SiteList.as_view(), name='site_list'),
    path('api/site_list/<int:site_id>', SiteDetail.as_view(), name='site_list'),
    path('api/yard_list', YardList.as_view(), name='yard_list'),
    path('api/yard_list/<int:yard_id>', YardDetail.as_view(), name='yard_list'),
    path('api/transaction_list', TransactionList.as_view(), name='transaction_list'),
    path('api/transaction_list/<int:transactions_id>', TransactionDetail.as_view(), name='transaction_list'),
    path('api/driver_list', DriverList.as_view(), name='driver_list'),
    path('api/driver_list/<int:driver_id>', DriverDetail.as_view(), name='driver_list'),
    path('api/auth', views.obtain_auth_token, name='obtain_auth_token'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)