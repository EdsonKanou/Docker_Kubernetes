from django.contrib import admin
from django.urls import path,include
from shop import views

urlpatterns = [
    path('', views.home, name='home'),
    path('details',views.details,name='details'),

]
