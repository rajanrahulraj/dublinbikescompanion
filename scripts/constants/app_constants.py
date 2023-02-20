import configparser

config = configparser.ConfigParser()
config.read('../../config/app_config.conf')


class DataSource:
    API_KEY = config.get("JCDecaux", "API_KEY")
    CONTRACT = config.get("JCDecaux", "CONTRACT")
    DYNAMIC_DATA_API = f"https://api.jcdecaux.com/vls/v1/stations?contract={CONTRACT}&apiKey={API_KEY}"


class DB:
    HOST = config.get("SQL", "host")
    PORT = config.get("SQL", "port")
    USER = config.get("SQL", "user")
    PASSWORD = config.get("SQL", "password")
    DATABASE = config.get("SQL", "database")
