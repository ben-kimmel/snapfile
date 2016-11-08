import webapp2
from google.appengine.api import users
from handlers import base_handlers
from models import DirectShare
import utils
    

class ShareHandler(base_handlers.BaseAction):
    def handle_post(self, user, email):
        print(self.request)
        for email_2 in self.request.get("emails").split(";"):
            share = DirectShare(parent=utils.get_parent_key_for_email(email))
            share.file = self.request.get("file_key")
            file.available_from = self.request.get("start")
            file.available_until = self.request.get("end")
            file.email = self.request.get(email_2)
            file.put()
        self.redirect("/files")