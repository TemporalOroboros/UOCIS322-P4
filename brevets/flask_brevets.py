"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
from flask import request
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import config

import logging

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY

###
# Pages
###

@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')

###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############

@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', None, type=float)
    brevet = request.args.get('brevet', 200, type=float)
    iso_start_time = request.args.get('start_time', arrow.now().isoformat, type=str)
    start_time = arrow.get(iso_start_time)

    if not km is None:
        open_time = acp_times.open_time(km, brevet, start_time).format('YYYY-MM-DDTHH:mm')
        close_time = acp_times.close_time(km, brevet, start_time).format('YYYY-MM-DDTHH:mm')
    else:
        open_time = ""
        close_time = ""
    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)

###
# Error Handlers
###

@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404

#############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")

