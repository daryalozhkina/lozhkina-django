from django.contrib.auth.models import User
from django.db import models
from mainapp.models import Books

class BookBasket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ForeignKey(Books, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.added.strftime("%Y.%m.%d %H:%M")}: {self.books.name}'

    def to_html(self):
        return f'{self.added.strftime("%Y.%m.%d %H:%M")}</i>: <b>{self.books.name}</b>'
# Create your models here.

