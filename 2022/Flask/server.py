import flask

app = flask.Flask(__name__)

"""
	A Flask server
	New HTML templates in <./templates>
	New static file in <./statics>
"""


@app.route("/")
def mainpage():
	return flask.render_template("index.html")

		
def main():
	try:
		app.run()
	except:
		pass
