import os
import jinja2
import webapp2
from handlers import BaseHandler
from models import Program

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
        [os.path.join(os.path.dirname(__file__),"../../../templates/admin"),
         os.path.join(os.path.dirname(__file__),"../../../templates/layouts")]))

LEGACY_TEMPLATE = JINJA_ENVIRONMENT.get_template('new_programs.html')

class AdminProgramNewHandler(BaseHandler.BaseHandler):
  def get(self):

    role = self.session.get('role')
    user_session = self.session.get("user")

    if role != "admin":
      self.redirect("/users/login?message={0}".format("You are not authorized to view this page"))
      return

    if not self.legacy:
      self.redirect("/#/admin/programs/new")

    form = Program.NewProgramForm()
    template_values = {
      "form": form,
      "user_session": user_session
    }
    self.response.write(LEGACY_TEMPLATE.render(template_values))

  def post(self):
    form = Program.NewProgramForm(self.request.POST)
    if form.validate():
      user = Program.save(self, form, LEGACY_TEMPLATE)
    else:
      self.response.write(LEGACY_TEMPLATE.render({"form": form}))
