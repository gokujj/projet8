import pytest

from users.models import User


@pytest.fixture
def user(transactional_db):
    yield User.objects.create_user(
        "testuser", "testuser@oc.com", "asdnFSdh7sd8Fa8f"
    )


def test_user_can_log_in_with_correct_email_and_password(
    user, driver, live_server
):
    """Tests user can log in with correct email and passwords."""
    driver.get(live_server.url)
    driver.find_element_by_css_selector("#menu--login").click()
    driver.find_element_by_css_selector("#id_login").send_keys(
        "testuser@oc.com"
    )
    driver.find_element_by_css_selector("#id_password").send_keys(
        "asdnFSdh7sd8Fa8f"
    )
    driver.find_element_by_css_selector("#id_login_button").click()
    driver.find_element_by_css_selector("#menu--user")
    driver.find_element_by_css_selector("#menu--carrot")
    driver.find_element_by_css_selector("#menu--logout").click()
    driver.find_element_by_css_selector(".btn-primary").click()
    driver.find_element_by_css_selector("#menu--login")


def test_user_cannot_log_in_with_wrong_password(user, driver, live_server):
    driver.get(live_server.url)
    driver.find_element_by_css_selector("#menu--login").click()
    driver.find_element_by_css_selector("#id_login").send_keys(
        "testuser@oc.com"
    )
    driver.find_element_by_css_selector("#id_password").send_keys(
        "openclassrooms"
    )
    driver.find_element_by_css_selector("#id_login_button").click()

    # assest alert div is present
    alert = driver.find_element_by_css_selector(".alert-danger ul li")
    assert alert.text == 'L’adresse e-mail ou le mot de passe sont incorrects.'
