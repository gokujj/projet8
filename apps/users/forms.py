from django.contrib.auth import forms
from django.contrib.auth import get_user_model


class UserCreationForm(forms.UserCreationForm):
    """Form managing data entry to create new
    users."""

    class Meta(forms.UserCreationForm.Meta):
        model = get_user_model()
        fields = ['email', 'username']


class UserChangeForm(forms.UserChangeForm):
    """Form managing data entry to update a user's information."""

    class Meta(forms.UserChangeForm.Meta):
        model = get_user_model()
        fields = ['email', 'username']
