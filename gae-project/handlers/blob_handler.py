from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.api import users
import utils
from models import DirectShare, File
import datetime

# Straight from https://cloud.google.com/appengine/docs/python/blobstore/
class BlobServer(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, blob_key):
        if not blobstore.get(blob_key):
            self.error(404)
        else:
            user = users.get_current_user()
            email = user.email().lower()
            parent_key = utils.get_parent_key_for_email(email)
            b_k = blobstore.get(blob_key).key()
            is_owner = File.query(File.blob_key == b_k, ancestor=parent_key).count() > 0
            is_shared = DirectShare.query(DirectShare.email == email, DirectShare.file == b_k).count() > 0
            is_public = File.query(File.blob_key == b_k, File.public == True).count() > 0
            
            share = DirectShare.query(DirectShare.email == email, DirectShare.file == b_k).get()
            in_time = False
            if share:
                start = share.available_from
                end = share.available_until
                now = datetime.datetime.utcnow()
                print(start)
                print(end)
                print(now)
                in_time = now > start and now < end
            print(in_time)
            
            if (is_owner or (is_shared and in_time) or is_public):
                self.send_blob(blob_key)
            else:
                self.error(403)