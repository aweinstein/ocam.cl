#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Alejandro Weinstein'
SITENAME = u"AJW's site"
SITEURL = 'http://www.ocam.cl'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

THEME = 'ocam-theme'

# Blogroll
LINKS =  ()

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/ajweinstein'),
          ('github', 'http://github.com/aweinstein'),
          ('gplus', 'https://plus.google.com/u/0/104593724053901106301'))


DEFAULT_PAGINATION = 10

DISPLAY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images',
                'pdfs']
