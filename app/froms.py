"""
Module defining HTML forms
"""
from flask_wtf import FlaskForm
from wtforms.fields import SubmitField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired
from flask_babel import lazy_gettext as _l


class VideoUrlForm(FlaskForm):
    """
    Form containing field for url of video
    that user want to download
    """
    video_url = URLField(_l('Link'), validators=(DataRequired(), ))
    submit = SubmitField(_l('Submit'))
