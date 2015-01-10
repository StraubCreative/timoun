import os
import jinja2
import webapp2
import logging

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname( __file__ ), '..', 'templates')))

TEMPLATE = JINJA_ENVIRONMENT.get_template('base.html')
LEGACY_TEMPLATE = JINJA_ENVIRONMENT.get_template('index.html')

class MainHandler(webapp2.RequestHandler):
  def get(self):
    logging.info(self.request.headers['User-Agent'])
    template_values = {}
    self.response.write(LEGACY_TEMPLATE.render(template_values))