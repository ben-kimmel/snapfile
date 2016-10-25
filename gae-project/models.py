from google.appengine.ext import ndb
from google.appengine.ext.ndb import msgprop
from protorpc.messages import Enum
from google.appengine.ext.db import BlobProperty


# TODO: Implement



class User(ndb.Model):
    username = ndb.StringProperty()
    
class File(ndb.Model):
    name = ndb.StringProperty()
    file = ndb.BlobProperty()
    owner_key = ndb.KeyProperty(kind=User)
    size = ndb.StringProperty()
    
class DirectShare(ndb.Model):
    available_until = ndb.DateTimeProperty()
    file = ndb.KeyProperty(kind=File)
    shared_with = ndb.KeyProperty(kind=User)
    



    