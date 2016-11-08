
from google.appengine.api import users
import webapp2
from google.appengine.ext.webapp import blobstore_handlers

import main
import utils
import logging
import os
import cloudstorage as gcs
from google.appengine.api import app_identity

# Potentially helpful (or not) superclass for *logged in* pages and actions (assumes app.yaml gaurds for login)

### Pages ###
class BasePage(webapp2.RequestHandler):
  """Page handlers should inherit from this one."""
  def get(self):
    user = users.get_current_user()
    values = {}
    self.update_values(user, values)
    template = main.jinja_env.get_template(self.get_template())
    self.response.out.write(template.render(values))


  def update_values(self, user, values):
    # Subclasses should override this method to add additional data for the Jinja template.
    pass


  def get_template(self):
    # Subclasses must override this method to set the Jinja template.
    raise Exception("Subclass must implement handle_post!")



### Actions ###

class BaseAction(blobstore_handlers.BlobstoreUploadHandler):
  """ALL action handlers should inherit from this one."""
  def post(self):

    user = users.get_current_user()
    email = user.email().lower()
    if not user:
      raise Exception("Missing user!")
    self.handle_post(user, email)


  def get(self):
    self.post()  # Action handlers should not use get requests.


  def handle_post(self, user, account_info):
    # Subclasses must override this method to handle the requeest.
    raise Exception("Subclass must implement handle_post!")
