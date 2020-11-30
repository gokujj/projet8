import pytest
from django.contrib.auth import get_user_model
from allauth.account.models import EmailAddress

User = get_user_model()


@pytest.fixture
def user(transactional_db):
    """Fixture creating a user with a verified email."""
    user = User.objects.create_user(
        "testuser", "testuser@oc.com", "asdnFSdh7sd8Fa8f"
    )
    EmailAddress.objects.create(
        user=user, email="testuser@oc.com", verified=True, primary=True
    )
    yield user