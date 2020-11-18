from .forms import SearchForm


def get_search_form(request):
    """Context processor providing the search form to each
    view of the project."""
    return {'search_form': SearchForm()}
