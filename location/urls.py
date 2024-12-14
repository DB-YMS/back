from django.urls import path
from .views import (
    YardCreateView, YardUpdateView, YardDeleteView, YardListView,
    SiteCreateView, SiteUpdateView, SiteDeleteView, SiteListView,
    DivisionCreateView, DivisionUpdateView, DivisionDeleteView, DivisionListView,
    MasterCreateView, MasterUpdateView, MasterDeleteView, MasterListView,
)

urlpatterns = [
    path('yard/', YardCreateView.as_view(), name='yard_create'),
    path('yard/all/', YardListView.as_view(), name='yard_list'),
    path('yard/<int:pk>/update/', YardUpdateView.as_view(), name='yard_update'),
    path('yard/<int:pk>/delete/', YardDeleteView.as_view(), name='yard_delete'),
    path('site/', SiteCreateView.as_view(), name='site_create'),
    path('site/all/', SiteListView.as_view(), name='site_list'),
    path('site/<int:pk>/update/', SiteUpdateView.as_view(), name='site_update'),
    path('site/<int:pk>/delete/', SiteDeleteView.as_view(), name='site_delete'),
    path('division/', DivisionCreateView.as_view(), name='division_create'),
    path('division/all/', DivisionListView.as_view(), name='division_list'),
    path('division/<int:pk>/update/', DivisionUpdateView.as_view(), name='division_update'),
    path('division/<int:pk>/delete/', DivisionDeleteView.as_view(), name='division_delete'),
    path('master/', MasterCreateView.as_view(), name='master_create'),
    path('master/all/', MasterListView.as_view(), name='master_list'),
    path('master/<int:pk>/update/', MasterUpdateView.as_view(), name='master_update'),
    path('master/<int:pk>/delete/', MasterDeleteView.as_view(), name='master_delete'),
]