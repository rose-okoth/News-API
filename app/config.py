class Config:
    '''
    General configuration parent class
    '''

    api_key = 'api_key',
    news_api_base_url = 'news_api_base_url'

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
