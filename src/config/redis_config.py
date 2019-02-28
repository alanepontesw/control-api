import os

class RedisConfig:
    HOST = os.environ.get('REDIS_HOST') or '127.0.0.1'
    PASSWORD = os.environ.get('REDIS_PASSWORD')
    PORT = os.environ.get('REDIS_PORT') or '6379'
    DATABASE = os.environ.get('REDIS_DATABASE')
    