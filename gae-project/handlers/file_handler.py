import webapp2
from google.appengine.api import users
from handlers import base_handlers

class FileHandler(base_handlers.BasePage):
    
    def get_template(self):
        return "templates/files.html"
    
    def update_values(self, user, values):
        values["logout_url"] = users.create_logout_url("/")