from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import sentry_sdk

from apiclients.clients import OpenfoodfactsClient
from apiclients.validators import ProductValidator
from apiclients.normalizers import ProductNormalizer
from products.models import Product


class Command(BaseCommand):
    help = 'Updates product data from the openfoodfacts API'

    def handle(self, *args, **options):
        client = OpenfoodfactsClient()
        validator = ProductValidator()
        normalizer = ProductNormalizer()

        # Download data from openfoodfacts
        self.stdout.write(
            self.style.SUCCESS('Updating products from openfoodfacts...')
        )
        sentry_sdk.capture_message('Updating products from openfoodfacts...')

        products = client.get_products_by_popularity(
            page_size=settings.PRODUCT_CLIENT_PAGE_SIZE,
            number_of_pages=settings.PRODUCT_CLIENT_NUMBER_OF_PAGES * 2,
        )
        # Validate data
        products = validator.filter(products)
        # Normalize data
        normalizer.normalize_all(products)

        Product.objects.update_from_openfoodfacts(products)