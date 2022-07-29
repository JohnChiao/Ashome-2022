import flask

app = flask.Flask(__name__)


@app.route("/")
def mainpage():
	return flask.render_template("index.html")


@app.route("/about")
def abpage():
	return flask.render_template("about.html")


@app.route("/gt")
def gitpage():
	return flask.render_template("gt.html")


def main():
	input("Page:")
	app.run()