from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.urls import reverse

from ..forms import FavoriteCreationForm
from ..models import Favorite


class FavoriteListApiView(LoginRequiredMixin, View):
    """Vue responsable d'ajouter un favori à la liste de favori de
    l'utilisateur.
    """

    def post(self, request, *args, **kwargs):
        """Ajoute un nouveau favori à la liste de l'utilisateur."""
        form = FavoriteCreationForm(data=request.POST)
        if not form.is_valid():
            return HttpResponseNotFound()
        fav, created = form.save(user=request.user)
        return JsonResponse(
            {
                'url': reverse('favorites_api:detail', kwargs={'pk': fav.id}),
            },
            status=201 if created else 200,
        )


class FavoriteApiView(LoginRequiredMixin, View):
    """Gère les opération sur un favori identifié par son produit et son
    substitut."""

    def delete(self, request, pk, *args, **kwargs):
        """Efface un favoris de la liste des favoris de l'utilisateur."""
        try:
            favorite = Favorite.objects.get(id=pk, user=request.user)
        except Favorite.DoesNotExist:
            return HttpResponseNotFound()
        favorite.delete()
        return HttpResponse(status=204)
