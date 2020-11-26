"""Définit des filtres et tags pour faciliter la mise en place de la 
pagination."""

from django import template
from django.conf import settings

register = template.Library()

PAGINATION_DEFAULT_NEIGHBORS = getattr(
    settings, 'PAGINATION_DEFAULT_NEIGHBORS', 5
)


@register.filter
def page_range(
    paginator, current_page, neighbors=PAGINATION_DEFAULT_NEIGHBORS
):
    """Limite les pages affichées à un certain nombre de voisin autour de la
    page courrante."""
    if paginator.num_pages > 2 * neighbors + 1:
        first_page = max(1, current_page.number - neighbors)
        last_page = min(paginator.num_pages, current_page.number + neighbors)
        return range(first_page, last_page + 1)
    return paginator.page_range


@register.simple_tag(takes_context=True)
def query_string(context, **kwargs):
    """Ajoute ou remplace un paramètre dans la query string à la requête
    courante."""
    qs = context['request'].GET.copy()
    for key, value in kwargs.items():
        qs[key] = value
    for key in [key for key, value in qs.items() if not value]:
        del qs[key]
    return qs.urlencode()
