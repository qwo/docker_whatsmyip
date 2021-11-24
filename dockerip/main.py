#!/usr/bin/python3
""" Demonstrating Flask, using APScheduler. """

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, request, jsonify, Response

import requests
import logging
import json
import os


app = Flask(__name__)

def sensor():
    """ Function for test purposes. """
    print("Ran job!")
    URL = os.environ.get("URL", "http://google.com")
    print(requests.get(URL).headers)
    return 



@app.route("/")
def home():
    """ Function for test purposes. """
    # Response.headers['Content-Type'] = 'application/json'
    response = jsonify({"access_routes": request.access_route, "headers": dict(request.headers)})

    app.logger.info(response)
    print("@@@@Access Route:", request.access_route)
    sensor()
    return response

sched = BackgroundScheduler(daemon=True, timezone="Europe/Berlin")
sched.add_job(sensor,'interval', minutes=5)
sched.start()


if __name__ == "__main__":
    sensor()
    app.run()