#coding:UTF-8
import os
import urllib
import jinja2
import webapp2

import cgi
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class TempData(ndb.Model):
	data1 = ndb.StringProperty()
	data2 = ndb.StringProperty()
	date = ndb.DateTimeProperty(auto_now_add=True)

	@classmethod
	def query_data(cls, ancestor_key):
		return cls.query(ancestor=ancestor_key).order(-cls.date)

class MainPage(webapp2.RequestHandler):

	def get(self):
		ancestor_key = ndb.Key("Data", "temp_data")
		temp_data = TempData.query_data(ancestor_key).fetch(50)

		dt = self.request.get('dt')
		tm = self.request.get('tm')
		
		template_values = {
			'dt':dt,
			'tm':tm,
			'temp_data': temp_data
		}

		# データ表示
		#for temp in temp_data:
		#	self.response.out.write('%s->%s<br>' % (temp.data1, temp.data2))

		t = JINJA_ENVIRONMENT.get_template("showdata.html")
		self.response.write(t.render(template_values))


application = webapp2.WSGIApplication([
    ('/.*', MainPage),
], debug=True)
