import mainapp.views as mainapp
from django.urls import path

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('catalog/', mainapp.catalog, name='catalog'),

    path('catalog/category/<int:category_pk>/', mainapp.catalog_page, name='catalog_page'),
    path('catalog/books/<int:books_pk>/', mainapp.books_page, name='books_page'),
]
