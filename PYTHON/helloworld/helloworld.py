#coding:UTF-8
import webapp2
import datetime
import locale

locale.setlocale(locale.LC_ALL, 'da_DK.UTF-8')

HTML = """\
	<!DOCTYPE html>
	<html lang="ja">
	<head>
	<meta charset="UTF-8">
	</head>
	<body>
	%s
	%s
	</body>
	</html>
"""

class MainPage(webapp2.RequestHandler):


	def get(self):
		#self.response.headers['Content-Type'] = 'text/html'
		greet_str = '<h1>Hello, World!</h1>'

		d = datetime.datetime.today()
		time_str = '<h2>%s時%s分%s.%s秒<h2>' % (d.hour, d.minute, d.second, d.microsecond)

		self.response.write(HTML % ( greet_str, time_str))


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
