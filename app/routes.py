"""
Module defining app routes
"""
# app.__init__ contains workaround to cyclic-import
# pylint: disable=cyclic-import
from flask import request, render_template

from app import app
from .froms import VideoUrlForm
from .downloader import YoutubeDownloader


@app.route('/')
def index():
    """
    View function for main page
    """
    video_url_from = VideoUrlForm(request.args)
    context = {
        'video_url_form': video_url_from,
    }

    video_url = video_url_from.video_url.data
    if video_url:
        downloader = YoutubeDownloader(video_url)
        available_downloads = downloader.get_available_downloads()
        context['available_downloads'] = available_downloads

    return render_template('index.html', **context)
