#coding:UTF-8
import os
import urllib

import jinja2
import webapp2
import datetime
import locale

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):

	def get(self):


		template_values = { 

		}

		path = self.request.path

		if path == "/datetime":

			html_template = "datetime.html"

		elif path == "/" or path.find("^index"):

			html_template = "index.html"
			template_values = {
				'msg': u"こんにちは",
				'url': self.request.url,
				'path': self.request.path
			}

		else:

			html_template = "err.html"
		
		t = JINJA_ENVIRONMENT.get_template(html_template)
		self.response.write(t.render(template_values))


application = webapp2.WSGIApplication([
    ('/.*', MainPage),
], debug=True)
