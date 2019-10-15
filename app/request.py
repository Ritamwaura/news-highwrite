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

def get_news_sources(category):
    '''
    Function that gets the json responce to our url request
    '''
    get_news_source_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_source_url) as url:
        get_news_source_data = url.read()
        get_news_source_response = json.loads(get_news_source_data)

        news_source_results = None

        if get_news_source_response['sources']:
            news_source_results_list = get_news_source_response['sources']
            news_source_results = process_results(news_source_results_list)
    return news_source_results
def get_news_source():
    '''
    Function that gets the json responce to our url request
    '''
    get_news_source_url = base_url.format(base_url,api_key)

    with urllib.request.urlopen(get_news_source_url) as url:
        get_news_source_data = url.read()
        get_news_source_response = json.loads(get_news_source_data)

        news_source_results = None

        if get_news_source_response['sources']:
            news_source_results_list = get_news_source_response['sources']
            news_source_results = process_results(news_source_results_list)


    return news_source_results


def process_results(news_source_results):
    '''
    Function  that processes the news source result and transform them to a list of Objects
    Args:
        news_sources_list: A list of dictionaries that contain news details
    Returns :
        news_source_results: A list of news sources objects
    '''
    news_sources_results = []
    
    for news_source_item in news_sources_results:
        id = news_source_item.get('id')
        name = news_source_item.get('name')
        description = news_source_item.get('description')
        url = news_source_item.get('url')
        language = news_source_item.get('language')
        category = news_source_item.get('category')
        
        if language == 'en':
            news_source_object = news_Source(id,name,description,url,language,category)
            news_sources_results.append(news_source_object)

    return news_source_results
