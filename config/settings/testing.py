from .base import *

CHROMEDRIVER_PATH = str(BASE_DIR / 'webdrivers' / 'chromedriver')
GECKODRIVER_PATH = str(BASE_DIR / 'webdrivers' / 'geckodriver')

CHROMEDRIVER_OPTIONS = ['--headless', 'window-size=1920x1080']
GECKODRIVER_OPTIONS = ['-headless']
