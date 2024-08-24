#it!/usr/bin/python3
""" Starts a flask application
This web application is listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
"""
from flask import Flask

app = Flask(__name__)


@app.route("/airbnb-onepage/", strict_slashes=False)
def hello_h():
    """ Method that displays 'Hello HBNB!' """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
