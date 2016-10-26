import webapp2
from google.appengine.api import users
from handlers import base_handlers
from google.appengine.ext.webapp import blobstore_handlers
import google.appengine.api.blobstore.blobstore as blobstore
from models import File

class FileHandler(base_handlers.BasePage):
    
    def get_template(self):
        return "templates/files.html"
    
    def update_values(self, user, values):
        values["logout_url"] = users.create_logout_url("/")
        values["upload_url"] = blobstore.create_upload_url("/files")
    
    def post(self):
        file = File()
        media_blob = self.get_uploads()[0]
        print(media_blob)
        file.key = media_blob.key()
        file.filename = media_blob.name()
        file.name = self.request.get("name")
        file.put()
        self.redirect("/files")