import urllib.request,json
from .models import news_Source

# Getting api key
api_key = None

# Getting the movie base url
base_url = None
articles_url=None
def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    # articles_url=app.config['NEWS_API_ARTICLES_URL']


