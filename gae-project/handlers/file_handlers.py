import webapp2
from google.appengine.api import users
from handlers import base_handlers
from google.appengine.ext.webapp import blobstore_handlers
import google.appengine.api.blobstore.blobstore as blobstore
from google.appengine.api.blobstore.blobstore import BlobKey
from models import File
from google.appengine.ext.blobstore.blobstore import BlobInfo
import utils


class FileHandler(base_handlers.BasePage):
    
    def get_template(self):
        return "templates/files.html"
    
    def update_values(self, user, values):
        values["logout_url"] = users.create_logout_url("/")
        values["upload_url"] = blobstore.create_upload_url("/upload")
        email = user.email().lower()
        values["my_files"] = utils.get_query_for_all_files_for_email(email)


class UploadHandler(base_handlers.BaseAction):
    def handle_post(self, user, email):
        upload = self.get_uploads()[0]
        print(self.request)
        file = File(parent=utils.get_parent_key_for_email(email))
        file.key = upload.key()
        file.file_name = upload.filename
        file.name = self.request.get("fileName")
        file.put()
        self.redirect("/files")
        
class DeleteHandler(base_handlers.BaseAction):
    def handle_post(self, user, email):
        file = self.request.get("file")
        