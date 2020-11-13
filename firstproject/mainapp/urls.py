"""firstproject URL Configuration

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
import mainapp.views as mainapp
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', mainapp.index, name='index'),
    path('catalog/', mainapp.catalog, name='catalog'),
    path('catalog/category/<int:category_pk>/', mainapp.catalog_page, name='catalog_page'),
    path('catalog/books/<int:books_pk>/', mainapp.books_page, name='books_page'),
    path('basket/<int:basket_pk>/', mainapp.basket, name='basket'),
    path('auth', authapp.urls, namespace='login'),
    path('admin/', admin.site.urls),

]

