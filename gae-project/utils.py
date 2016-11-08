import logging
from models import File
from google.appengine.ext import ndb



# TODO: Implement




# Potentially helpful (or not) NDB Snippets - For reference only
def get_parent_key_for_email(email):
    """ Gets the parent key (the key that is the parent to all Datastore data for this user) from the user's email. """
    return ndb.Key("Entity", email.lower())

def get_query_for_all_files_for_email(email):
    """ Returns a query for all OBJECTS for this user. """
    parent_key = get_parent_key_for_email(email)
    return File.query(ancestor=parent_key)