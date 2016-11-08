import os

import jinja2
import webapp2
from handlers import login_handler, file_handlers, blob_handler, share_handler

# Jinja environment instance necessary to use Jinja templates.
def __init_jinja_env():
    jenv = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions=["jinja2.ext.do", "jinja2.ext.loopcontrols", "jinja2.ext.with_"],
        autoescape=True)
    # Example of a Jinja filter (useful for formatting data sometimes)
    #   jenv.filters["time_and_date_format"] = date_utils.time_and_date_format
    return jenv

jinja_env = __init_jinja_env()

app = webapp2.WSGIApplication([
    ('/', login_handler.LoginHandler),
    ('/files', file_handlers.FileHandler),
    ('/upload', file_handlers.UploadHandler),
    ('/view/([^/]+)?', blob_handler.BlobServer),
    ('/share', share_handler.ShareHandler),
    ('/delete', file_handlers.DeleteHandler) 
], debug=True)
