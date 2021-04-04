"""
Module defining app routes
"""
# app.__init__ contains workaround to cyclic-import
# pylint: disable=cyclic-import
from app import app


@app.route('/')
def index():
    """
    View function for main page
    """
    return 'index'
