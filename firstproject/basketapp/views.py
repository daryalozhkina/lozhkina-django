from django.shortcuts import render
from django.urls import reverse
from mainapp.models import Books

def index(request):
    return render(request, 'basketapp/basket.html')

def add (request, books_id):
    books = Books.objects.get(pk=books_id)
    BookBasket.objects.get_or_create(
       user=request.user,
       books=books
    )
    # return HttpResponseRedirect(request.META.get())
    return HttpResponseRedirect(
        reverse('mainapp:catalog_page',
                kwargs={'category_pk': books.category_id})
    )