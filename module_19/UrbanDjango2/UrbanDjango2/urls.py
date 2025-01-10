"""
URL configuration for UrbanDjango2 project.

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
from django.contrib import admin  # type: ignore
from django.urls import path  # type: ignore
from task1.views import platform, store, cart, sign_up_by_html, django_sign_up, news

urlpatterns = [
    path('admin/', admin.site.urls),
    path('platform/cart/', cart),
    path('platform/store/', store),
    path('platform/', platform),
    path('', sign_up_by_html),
    path('django_sign_up/', django_sign_up),
    path('platform/news/', news),
]
