import webapp2
from google.appengine.api import users
from handlers import base_handlers

class LoginHandler(base_handlers.BasePage):
    
    def get_template(self):
        return "templates/login.html"
    
    def update_values(self, user, values):
        values["login_url"] = users.create_login_url("/files")