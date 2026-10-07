class BaseConfig():
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin@localhost/db_practice'
    JWT_SECRET_KEY = 'secreta-senha-secreta-senha-secreta-senha-secreta-senha'

class DevelopmentConfig():
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin@localhost/db_practice'
    JWT_SECRET_KEY = 'minha-senha-secreta-minha-senha-secreta-minha-senha-secreta'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig():
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:admin@localhost/db_practice"
    JWT_SECRET_KEY = 'random_password_random_password_random_password_random_password_random_password'
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

configs = {"DevelopmentConfig":DevelopmentConfig, "TestingConfig":TestingConfig}