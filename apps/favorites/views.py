from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator

from .models import Favorite


@method_decorator(ensure_csrf_cookie, name='dispatch')
class FavoriteListView(LoginRequiredMixin, ListView):
    """Vue gérant l'affichage de la liste des favoris de l'utilisateur
    connecté."""

    template_name = 'favorites/list.html'
    model = Favorite
    context_object_name = 'favorites'

    def get_queryset(self):
        """Filtre les objets récupérés pour obtenir uniquement ceux qui
        appartiennent à l'utilisateur."""
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
