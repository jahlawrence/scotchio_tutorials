# config.py one variable per line

# if enable debug. make sure its false in production 
# Put any configurations here that are common across all environments

class Config(object):
    """
    Common Configs
    """

class DevelopmentConfig(Config):
    """
    Dev Configs
    """


    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """


    DEBUG = False
  

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig

}
