import webapp2
from google.appengine.ext import blobstore
from google.appengine.api import users
from handlers import base_handlers
from models import DirectShare
import utils
from datetime import datetime as dt
    

class ShareHandler(base_handlers.BaseAction):
    def handle_post(self, user, email):
        print(self.request)
        print(self.request.get("public"))
        for email_2 in self.request.get("emails").split(";"):
            print(email_2)
            if self.request.get("file_key") and self.request.get("start") and self.request.get("end"):
                share = DirectShare(parent=utils.get_parent_key_for_email(email))
                share.file = blobstore.get(self.request.get("file_key")).key()
                share.available_from = dt.strptime(self.request.get("start"), "%Y-%m-%dT%H:%M")
                share.available_until = dt.strptime(self.request.get("end"), "%Y-%m-%dT%H:%M")
                share.email = email_2
                share.put()
        self.redirect("/files")