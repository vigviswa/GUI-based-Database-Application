from os import getenv


class AppConfig(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False
    SECRET_KEY = getenv("SECRET_KEY")
    MYSQL_HOST = getenv("MYSQL_HOST")
    MYSQL_USER = getenv("MYSQL_USER")
    MYSQL_PASSWORD = getenv("MYSQL_PASSWORD")
    MYSQL_DB = getenv("MYSQL_DB")
    CLOUD_SQL_INSTANCE_NAME = getenv("CLOUD_SQL_INSTANCE_NAME")
    SQLALCHEMY_DATABASE_URI = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@/{MYSQL_DB}?unix_socket=/cloudsql/{CLOUD_SQL_INSTANCE_NAME}"


class DevelopmentConfig(AppConfig):
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return f"mysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_HOST}/{self.MYSQL_DB}"
