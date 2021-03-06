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

		d1 = self.request.get('data1')
		d2 = self.request.get('data2')

		# データ保存
		if d1!="99.99":
			temp_data = TempData(
					parent=ndb.Key("Data", "temp_data"),
					data1 = d1,
					data2 = d2
			)
			temp_data.put()

			self.response.out.write('done')
			
	def skip():
		ancestor_key = ndb.Key("Data", "temp_data")
		temp_data = TempData.query_data(ancestor_key).fetch(50)

		
		template_values = {
			'temp_data': temp_data
		}

		# データ表示
		for temp in temp_data:
			self.response.out.write('%s->%s<br>' % (temp.data1, temp.data2))



		t = JINJA_ENVIRONMENT.get_template("passdata.html")
		self.response.write(t.render(template_values))


application = webapp2.WSGIApplication([
    ('/.*', MainPage),
], debug=True)
