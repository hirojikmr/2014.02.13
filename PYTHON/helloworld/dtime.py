#coding:UTF-8
import os
import urllib

from datetime import datetime
import locale

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):

	def get(self):

		html_template = "index.html"

		d = datetime.today()
		time_str = u'%s時%s分%s.%s秒' % (d.hour, d.minute, d.second, d.microsecond)
		template_values = {
			'time_str': time_str
		}

		t = JINJA_ENVIRONMENT.get_template("dtime.html")
		self.response.write(t.render(template_values))


app = webapp2.WSGIApplication([
    ('/.*', MainPage),
], debug=True)
