"""
Downloading realization
"""
from youtube_dl import YoutubeDL
from youtube_dl.utils import DownloadError
from flask_babel import gettext as _

from config import Config

BYTES_IN_MEGABYTE = 10**6
BYTES_IN_GIGABYTE = 10**9
DEFAULT_VIDEO_TITLE = 'file'


class YoutubeDownloader(YoutubeDL):
    """
    Class encapsulating downloading logic.
    YoutubeDownloader objects contains information about video
    and possible download options, such as direct video url for
    every video/audio format, quality, size.
    """
    def __init__(self, video_url, *args, **kwargs):
        self.video_url = video_url
        self.available_downloads = None
        self.title = None
        super().__init__(*args, **kwargs)

    def get_available_downloads(self) -> dict:
        """
        Get available downloads for specified youtube
        video.
        :return: dict with such keys:
        title - video title
        videos - list of dicts, each dict representing
        available download, containing file size, direct
        url for downloading, formatted size, video quality
        and extension.
        """
        info = self.extract_info(self.video_url, download=False)
        title = info.get('title', DEFAULT_VIDEO_TITLE)
        self.available_downloads = {
            'title': title,
            'videos': [],
        }

        formats = info.get('formats')
        if not formats:
            raise DownloadError(_('No available downloads'))

        for fmt in formats:
            if (ext := fmt.get('ext')) not in Config.ALLOWED_EXTENSIONS:
                continue

            acodec = fmt.get('acodec')
            vcodec = fmt.get('vcodec')

            if 'none' not in (acodec, vcodec):
                size = fmt.get('filesize')
                formatted_size = self._get_formatted_size(size)
                self.available_downloads['videos'].append({
                    'ext': ext,
                    'size': size,
                    'url': fmt.get('url', ''),
                    'formatted_size': formatted_size,
                    'quality': fmt.get('format_note', '')
                })
        return self.available_downloads

    @staticmethod
    def _get_formatted_size(size: int) -> str:
        """
        Convert file size in bytes into user readable format
        Example: 40318629 to 40.32 Mb
        :param size: int, file size in bytes
        :return: str, size in Mb or Gb.
        """
        if not size:
            return ''
        if size >= BYTES_IN_GIGABYTE:
            return f'{round(size / BYTES_IN_GIGABYTE, 2)} Gb'

        return f'{round(size / BYTES_IN_MEGABYTE, 2)} Mb'
