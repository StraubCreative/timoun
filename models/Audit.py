from google.appengine.ext import ndb


CLEARANCE_OPTIONS = ["admin", "staff", "public"]
ACTIONS = ["Create Service", "Create Program", "Create Organization", "Create User", "Update User", "User Confirmation", "User Set Password", "Delete User", "Create Organization", "Edit Organization", "Delete Organization", "Create Program", "Update Program", "Delete Program", "Create Service", "Update Service", "Delete Service"]
MODELS = ["User", "Organization", "Program", "Service"]

class Audit(ndb.Model):
  initiated_by = ndb.StringProperty(required=True)
  user_affected =  ndb.StringProperty(required=False)
  organization_affected = ndb.StringProperty(required=False)
  security_clearance = ndb.StringProperty(required=True, choices=CLEARANCE_OPTIONS)
  json_data = ndb.TextProperty(required=True)
  model_affected = ndb.StringProperty(required=True, choices = MODELS)
  action = ndb.StringProperty(required=True, choices = ACTIONS)
  created_at = ndb.DateTimeProperty(auto_now_add=True, required=True)


def save(initiated_by, security_clearance, model, action, user_affected=None, organization_affected=None, json_data = ""):
  audit = Audit(initiated_by = initiated_by, user_affected = user_affected, security_clearance = security_clearance, json_data = json_data, model_affected = model, action = action, organization_affected=organization_affected)
  s = audit.put()
