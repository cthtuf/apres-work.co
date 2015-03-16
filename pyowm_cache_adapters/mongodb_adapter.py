#!/usr/bin/env python

from pyowm.abstractions.owmcache import OWMCache

class MongoDBAdapter(OWMCache):
  """
  Needs: pymongo bindings (https://pypi.python.org/pypi/pymongo/)
  
  Each cache items is a JSON document in the form:
  
    { "request_url": <request_url>,
      "response_json": <response_json>,
      "created_at": <utc_date>
    }
  
  where <request_url> and <response_json> are strings and <utc_date> is a UTC
  datetime.datetime object.
  """
  
  # Defaults:
  
  # cache item expiration time in seconds
  __ITEM_LIFETIME_SECONDS = 60*10 # Ten minutes
  
  # hostname and port
  __HOSTNAME = "127.0.0.1"
  __PORT = 27017
  
  # database and document collection
  __DATABASE = "pyowm"
  __COLLECTION = "cache"
  
  def __init__(self, hostname=__HOSTNAME, port=__PORT, database=__DATABASE,
               collection=__COLLECTION, item_lifetime=__ITEM_LIFETIME_SECONDS):
    from pymongo import MongoClient
    self._mongo = MongoClient(hostname, port)
    self._database = database
    self._collection = collection
    self._item_lifetime = item_lifetime
    self.setup_expiration(item_lifetime)
 
  def setup_expiration(self, item_lifetime):
    """
    Ensures that the collection has an index on the creation timestamp field
    and tells MongoDB to delete cache items (documents) that have been inserted
    more than "item_lifetime" ago into the collection.
    """
    from pymongo import ASCENDING
    self._mongo[self._database][self._collection].ensure_index(
        [("created_at", ASCENDING)], expireAfterSeconds=item_lifetime)

  def get(self, request_url):
    result =self._mongo[self._database][self._collection].find_one(
        {"request_url": request_url})
    if result:
        return result["response_json"].encode('utf-8')
    else:
        return None
 
  def set(self, request_url, response_json):
    from datetime import datetime
    cache_item = {"request_url": request_url,
                  "response_json": response_json,
                  "created_at": datetime.utcnow()}
    self._mongo[self._database][self._collection].insert(cache_item)