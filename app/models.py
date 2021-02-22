class News:
    '''
    News class to define news article objects
    '''
    def __init__(self,source,author,title,description,url,publishedAt,urlToImage):
        self.source=source
        self.author=author
        self.title=title
        self.description=description
        self.url=url
        self.publishedAt=publishedAt
        self.urlToImage=urlToImage

class Sources:
    '''
    Source class to define the news article sources
    '''
    def __init__(self,name,description,url,category,country):
        self.name=name
        self.description=description
        self.url=url
        self.category=category
        self.country=country
