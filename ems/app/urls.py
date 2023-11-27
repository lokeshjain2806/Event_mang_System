"""
URL configuration for ems project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from .views import Home, checkout, paymentdone, checkout2, checkout3, checkout4

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('checkout/', checkout, name='checkout'),
    path('checkout2/', checkout2, name='checkout2'),
    path('checkout3/', checkout3, name='checkout3'),
    path('checkout4/', checkout4, name='checkout4'),
    path('paymentdone/', paymentdone, name='paymentdone'),
]
