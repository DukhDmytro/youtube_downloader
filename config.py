"""
Configuration for Flask application
"""
# app.__init__ contains workaround to cyclic-import
# pylint: disable=too-few-public-methods, cyclic-import
import os


class Config:
    """
    Class containing settings for Flask app.
    """
    FLASK_APP = os.environ.get('FLASK_APP')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you_never_guess'
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
    ALLOWED_EXTENSIONS = ['mp4', ]
