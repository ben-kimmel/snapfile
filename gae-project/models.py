from google.appengine.ext import ndb
from google.appengine.ext.ndb import msgprop
from protorpc.messages import Enum
from google.appengine.ext.db import BlobProperty


# TODO: Implement



class File(ndb.Model):
    name = ndb.StringProperty()
    owner = ndb.StringProperty()
    file_name = ndb.StringProperty()
    blob_key = ndb.BlobKeyProperty()
    size = ndb.StringProperty()
    public = ndb.BooleanProperty(default=False)
    views = ndb.IntegerProperty(default=0)
    downloads = ndb.IntegerProperty(default=0)
    
    
class DirectShare(ndb.Model):
    available_from = ndb.DateTimeProperty()
    available_until = ndb.DateTimeProperty()
    file = ndb.BlobKeyProperty()
    email = ndb.StringProperty()



    