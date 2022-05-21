import os
from decouple import config

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
CHROMEDRIVER_PATH = config('CHROMEDRIVER_PATH', None)
DEBUG = config('DEBUG', False)
USERNAME = config('LINKEDIN_USERNAME', '')
PASSWORD = config('LINKEDIN_PASSWORD', '')
SENTRY_SDK = config('SENTRY_SDK', '')
LINKEDIN_LANDING_URL = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"

# Make sure that the url below has &page=n towards the end.
LINKEDIN_SEARCH_URL = "https://www.linkedin.com/search/results/people/?geoUrn=%5B%22102713980%22%5D&keywords=python&origin=FACETED_SEARCH&page=2"
