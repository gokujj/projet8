from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from apiclients.clients import OpenfoodfactsClient
from apiclients.validators import ProductValidator
from apiclients.normalizers import ProductNormalizer
from products.models import Product


class Command(BaseCommand):
    help = 'Downloads product data from the openfoodfacts API'

    def handle(self, *args, **options):
        client = OpenfoodfactsClient()
        validator = ProductValidator()
        normalizer = ProductNormalizer()

        # Télécharger les données depuis openfoodfacts
        self.stdout.write(
            self.style.SUCCESS('Downloading products from openfoodfacts...')
        )
        products = client.get_products_by_popularity(
            page_size=settings.PRODUCT_CLIENT_PAGE_SIZE,
            number_of_pages=settings.PRODUCT_CLIENT_NUMBER_OF_PAGES,
        )
        # Valider les données reçues
        products = validator.filter(products)
        # Normaliser les données reçues
        normalizer.normalize_all(products)

        Product.objects.create_from_openfoodfacts(products)