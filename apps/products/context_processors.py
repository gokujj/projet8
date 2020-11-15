from .forms import SearchForm


def get_search_form(request):
    """Processeur de contexte fournissant le formulaire de recherche à chaque
    vue du projet."""
    return {'search_form': SearchForm()}
