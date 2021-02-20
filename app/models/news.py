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
