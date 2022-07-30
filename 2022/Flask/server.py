import flask

app = flask.Flask(__name__)


@app.route("/")
def mainpage():
	return flask.render_template("index.html")


@app.route("/index.html")
def indexpage():
	return flask.render_template("index.html")


@app.route("/about.html")
def abpage():
	return flask.render_template("about.html")


@app.route("/gt.html")
def gitpage():
	return flask.render_template("gt.html")


def main():
	app.run()