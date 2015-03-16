#!/usr/bin/env python

from pyowm.abstractions.owmcache import OWMCache

class RedisAdapter(OWMCache):
  """
  Needs: redis-py bindings (https://pypi.python.org/pypi/redis/)
  """
  
  # Defaults:
  
  # cache item expiration time in seconds
  __ITEM_LIFETIME_SECONDS = 60*10 # Ten minutes
  
  # hostname and port
  __HOSTNAME = "127.0.0.1"
  __PORT = 6379
  
  def __init__(self, hostname=__HOSTNAME, port=__PORT, item_lifetime=__ITEM_LIFETIME_SECONDS):
    from redis import Redis
    self._redis = Redis(hostname, port)
    self._item_lifetime = item_lifetime
 
  def get(self, request_url):
    return self._redis.get(request_url)
 
  def set(self, request_url, response_json):
    self._redis.set(request_url, response_json, self._item_lifetime)
