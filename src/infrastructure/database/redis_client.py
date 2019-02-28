from redis import ConnectionPool, Redis
from config.redis_config import RedisConfig

class RedisClient:

    pool = None

    @staticmethod
    def _pool(host, port, password, database):
        if not RedisClient.pool:
            RedisClient.pool = ConnectionPool(host=host, port=port, password=password, db=database)
        return RedisClient.pool

    @staticmethod
    def connection(host=RedisConfig.HOST, port=RedisConfig.PORT, password=RedisConfig.PASSWORD, database=RedisConfig.DATABASE):
        return Redis(connection_pool=RedisClient._pool(host=host, port=port, password=password, database=database))

    # TODO : handler to race conditions problems
    # def pipeline(self):
    #     return self.connection().pipeline()

    def get_or_set(self, key, value, ex):
        item = self.get(key)
        if not item:
            self.set(key, value, ex)
            return (True, value)
        return (False, item)

    def set(self, key, value, ex=None):
        self.connection().set(key, value, ex)

    def get(self, key):
        return self.connection().get(key)

    # def getset(self, key, value):
    #     return self.connection().getset(key, value)

    # def delete(self, key):
    #     return self.connection().delete(key)

    # def rpush(self, key, value):
    #     return self.connection().rpush(key, *value)

    # def range(self, key):
    #     return self.connection().lrange(key, 0, -1)
