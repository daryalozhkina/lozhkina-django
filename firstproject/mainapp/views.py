from django.shortcuts import render

from mainapp.models import ProductCategory, Products


def index(request):
    return render(request, 'mainapp/index.html')


def catalog(request):
    categories = ProductCategory.objects.all()
    context = {
        'categories': categories,
        'page_title': 'каталог'
    }
    return render(request, 'mainapp/catalog.html')


def basket(request):
    return render(request, 'mainapp/basket.html')


def catalog_page(request, pk):
    courses = Products.objects.filter(category_id=pk)
    context = {
        'courses': courses,
        'page_title': 'страница каталога'
    }
    return render(request, 'mainapp/catalog_page.html', context)