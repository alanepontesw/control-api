import pickle
from infrastructure.database.redis_client import RedisClient

class ControlAPI:

    def __init__(self, redis_client=RedisClient(), ttl=10*60):
        self.redis_client = redis_client
        self.ttl = ttl

    def request_is_denied(self, request):
        created, _ = self.redis_client.get_or_set(key=request.hashify(), value=pickle.dumps(request), ex=self.ttl)
        return not created
