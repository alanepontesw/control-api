import os

# TODO: Handler with multi envs
class ControlAPIConfig:
    HOST = os.environ.get('HOST_API') or '0.0.0.0'
    TTL_REQUEST_API = os.environ.get('TTL_REQUEST_API') or 10*60
    