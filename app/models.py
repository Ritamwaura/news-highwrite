class news_Source:
    '''
    news_Source class to define news_Source Objects
    '''
    def __init__(self,newsid,author,title,description,url,urlToImage,publishedAt,content):
        self.newsid = newsid
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content

class news_Article:
    '''
    news_Article class to define news_Article Objects
    
    '''