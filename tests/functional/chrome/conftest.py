from django.conf import settings
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    """Fixture instanciating a webdriver.Chrome instance."""
    chrome_options = webdriver.ChromeOptions()
    for option in getattr(settings, 'CHROMEDRIVER_OPTIONS', []):
        chrome_options.add_argument(option)

    # Configuration of the chrome webdriver
    driver = webdriver.Chrome(
        executable_path=settings.CHROMEDRIVER_PATH,
        options=chrome_options,
    )
    driver.implicitly_wait(30)
    driver.maximize_window()

    yield driver
    # Teardown
    driver.quit()
