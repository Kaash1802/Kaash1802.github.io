import os
import sys
from urllib.parse import urlencode, parse_qsl

import xbmcgui
import xbmcplugin
from xbmcaddon import Addon
from xbmcvfs import translatePath

# Get the plugin url in plugin:// notation.
URL = sys.argv[0]
# Get a plugin handle as an integer number.
HANDLE = int(sys.argv[1])
# Get addon base path
ADDON_PATH = translatePath(Addon().getAddonInfo('path'))
ICONS_DIR = os.path.join(ADDON_PATH, 'resources', 'images', 'icons')
FANART_DIR = os.path.join(ADDON_PATH, 'resources', 'images', 'fanart')


def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.

    :param kwargs: "argument=value" pairs
    :return: plugin call URL
    :rtype: str
    """
    return '{}?{}'.format(URL, urlencode(kwargs))


def search_videos(query):
    """
    Simulates searching for videos based on a user query. 
    (Replace this function with your actual search logic using web scraping or APIs)

    :param query: user search query
    :type query: str
    :return: list of video dictionaries
    :rtype: list
    """

    # Replace this with your actual search implementation
    # This is just a placeholder to demonstrate search functionality
    videos = []
    if query.lower() == "Sports":
        videos = [
            {
                'title': 'Sky Sports News',
                'url': 'https://inst2.ignores.top/js/sky-sports-news-ssn-breaking-sports-news/1/playlist.m3u8',
                'poster': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTP63lQLR7Pxm9Jc5TH-mZbQ3k4aeY2kLExeREG_1o2aQ&s',
                'plot': '',
                'year': 2024,
            },
        ]
    return videos


def get_genres():
    """
    Hardcoded list of video genres for demonstration purposes.

    In a real addon, consider using an API to retrieve genres dynamically.
    """
    return [
        {'genre': 'Sports', 'icon': os.path.join(ICONS_DIR, 'Horror.png'), 'fanart': os.path.join(FANART_DIR, 'Horror.jpg')},
        {'genre': 'Comedy', 'icon': os.path.join(ICONS_DIR, 'Comedy.png'), 'fanart': os.path.join(FANART_DIR, 'Comedy.jpg')},
    ]


def get_videos(genre=None):
    """
    Retrieves video information based on genre or search query.

    :param genre: Optional genre to filter videos (default: None)
    :type genre: str
    :return: list of video dictionaries
    :rtype: list
    """
    if genre:
        # Simulate filtering videos based on genre (replace with actual logic)
        videos = []
        for genre_info in get_genres():
            if genre_info['genre'] == genre:
                videos = genre_info.get('movies', [])
                break
        return videos
    else:
        # No genre provided, so assume user search
        query = get_user_search()
        return search_videos(query)


def get_user_search():
    """
    Prompts the user for a search query using a Kodi dialog.
    """
