#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# general config
AUTHOR = 'Nicholas Zwart'
SITENAME = 'gpilab.com'
SITETITLE = 'GPI'
SITESUBTITLE = 'Graphical Programming Interface'
SITEURL = ''
STATIC_PATHS = ["images", "static"]

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'

PATH = 'content'
TIMEZONE = 'America/Phoenix'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10

# sitemap
PLUGINS=['extended_sitemap',]
EXTENDED_SITEMAP_PLUGIN = {
    'priorities': {
        'index': 1.0,
        'articles': 0.8,
        'pages': 0.5,
        'others': 0.4
    },
    'changefrequencies': {
        'index': 'daily',
        'articles': 'weekly',
        'pages': 'monthly',
        'others': 'monthly',
    }
}

# links
GITHUB_URL = 'https://github.com/gpilab'
YOUTUBE_URL= 'http://www.youtube.com/user/gpilab'
DOCUMENTATION_URL='http://docs.gpilab.com'

# footer
COPYRIGHT = '2016 Nicholas Zwart, Jim Pipe, Ashley Anderson'
#FOOTER_TEXT = 'hello'

# favicon
EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'},
    'images/favicon.png': {'path': 'favicon.png'},
    'static/CNAME':{'path': 'CNAME'}
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# theme specific
THEME = "./theme/clean-blog"
HEADER_COVER = '/images/banner.jpg'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
