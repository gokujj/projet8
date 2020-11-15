from django.contrib.auth import forms
from django.contrib.auth import get_user_model


class UserCreationForm(forms.UserCreationForm):
    """Formulaire gérant la saisie de données pour créer de nouveau
    utilisateurs."""

    class Meta(forms.UserCreationForm.Meta):
        model = get_user_model()
        fields = ['email', 'username']


class UserChangeForm(forms.UserChangeForm):
    """Formlaire gérant la saisie de données pour mettre à jours les infos
    d'un utilisateur."""

    class Meta(forms.UserChangeForm.Meta):
        model = get_user_model()
        fields = ['email', 'username']