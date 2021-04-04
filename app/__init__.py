"""
Module for Flask application initialization
"""
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Import at the bottom of the file - workaround
# to circular imports, a common problem with Flask applications.
# pylint: disable=wrong-import-position
from app import routes  # noqa:E402, F401
