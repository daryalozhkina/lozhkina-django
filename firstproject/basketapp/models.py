from django.contrib.auth.models import User
from django.db import models
from mainapp.models import Books

class BookBasket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ForeignKey(Books, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
# Create your models here.
