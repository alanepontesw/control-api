import hashlib
import json
class Request:

    def __init__(self, method, body):
        self.method = method
        self.body = body

    def hashify(self):
        key = self.method.lower() + json.dumps(self.body, sort_keys=True)
        return hashlib.md5(key.encode('utf-8')).hexdigest()
