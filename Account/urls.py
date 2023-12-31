from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', index,name='accounts_home' ),
    path('report/<int:pk>/', report,name='report' ),
    path('loan_page/', loan_system,name='loan_system' ),
]
