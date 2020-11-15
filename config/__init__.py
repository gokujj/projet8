from pathlib import Path 
import sys

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# Configure sys.path in order to import django applications from apps easily
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / 'apps'))