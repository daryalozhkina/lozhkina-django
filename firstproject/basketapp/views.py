from django.shortcuts import render

def index(request):
    return render(request, 'basketapp/basket.html')

# def add (request, books_name):
#     BookBasket.objects.get_or_create(
#         user=request.user,
#        course_id=books_name
#     )
#     # return HttpResponseRedirect(
#     #     reverse('mainapp:catalog_page',
#     #             kwargs={'category_pk': books.category_id})
#     # )             n