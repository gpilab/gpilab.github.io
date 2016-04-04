#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# general config
AUTHOR = 'Nicholas Zwart'
SITENAME = 'gpilab'
SITETITLE = 'GPI'
SITESUBTITLE = 'Graphical Programming Interface'
SITEURL = ''
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL

PATH = 'content'
TIMEZONE = 'America/Phoenix'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10

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
