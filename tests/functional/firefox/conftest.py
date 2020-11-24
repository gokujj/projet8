from django.conf import settings
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    """Fixture instanciating a webdriver.Firefox instance."""
    firefox_options = webdriver.FirefoxOptions()
    for option in getattr(settings, 'GECKODRIVER_OPTIONS', []):
        firefox_options.add_argument(option)

    # Configuration of the chrome webdriver
    driver = webdriver.Firefox(
        executable_path=settings.GECKODRIVER_PATH,
        options=firefox_options,
    )
    driver.implicitly_wait(30)
    driver.maximize_window()

    yield driver
    # Teardown
    driver.quit()