#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Alejandro Weinstein"
SITENAME = u"AJW's site"
SITEURL = 'http://www.ocam.cl'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG='en'

# Blogroll
LINKS =  (
    ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
    ('Python.org', 'http://python.org'),
    ('Jinja2', 'http://jinja.pocoo.org'),
    ('You can modify those links in your config file', '#')
         )

# Social widget
SOCIAL = (
          ('You can add links in your config file', '#'),
         )

DEFAULT_PAGINATION = False

DISPLAY_PAGES_ON_MENU = True

SOCIAL = (('twitter', 'http://twitter.com/ajweinstein'),
          ('github', 'http://github.com/aweinstein'),)

STATIC_PATHS = ['images',
                'pdfs']
