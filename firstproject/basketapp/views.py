from django.shortcuts import render
from django.urls import reverse
from mainapp.models import Books

def index(request):
    item = BookBasket.objects.filter(user =request.user)
    context = {
        'object_list': item,
    }
    return render(request, 'basketapp/basket.html', context)

def add (request, books_id):
    books = Books.objects.get(pk=books_id)
    BookBasket.objects.get_or_create(
       user=request.user,
       books=books
    )

def remove(request, books_basket_id):
    item = BookBasket.objects.get(id_=books.basket_id)
    item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
