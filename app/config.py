class Config:
    '''
    General configuration parent class
    '''
    # news_api_base_url ='https://newsapi.org/v2/?q=bitcoin&apiKey=8c39155e2f654098827b9fc8512d091b'
    # api_key ='8c39155e2f654098827b9fc8512d091b'

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
