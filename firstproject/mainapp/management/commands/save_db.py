import pickle

from django.core.management.base import BaseCommand

from mainapp.models import ProductCategory, Products

class Command(BaseCommand):
    help = 'copy of db in file'

    def handle(self, *args, **options):
        categories: ProductCategory.objects.all()
        with open('categories.bin', 'ct') as f:
            pickle.dump('categories', f)