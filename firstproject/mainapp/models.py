from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

class Books(models.Model):
    category = models.ForeignKey(ProductCategory,
                                 on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=200)
    desc = models.TextField('Описание', blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

