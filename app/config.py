class Config:
    '''
    General configuration parent class
    '''
    news_api_base_url ='https://newsapi.org/v2/endpoint/{}?api_key={}'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True