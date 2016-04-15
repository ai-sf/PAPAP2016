#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from time import strftime, localtime
import collections

SITENAME = "APAP"
AUTHOR = 'Giulio Pasqualetti'
#SITEURL = ''

RELATIVE_URLS = True

TIMEZONE = 'Europe/Brussels'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

'''
# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
'''

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DELETE_OUTPUT_DIRECTORY = True

DISPLAY_PAGES_ON_MENU = True

PATH = 'content/'

STATIC_PATHS = ['images','files','videos']

THEME = "themes/materializecss"

#MENUITEMS = [("personal", "https://ilfugiuliopascal.hopper.pw/")]
#MENUITEMS = [("personal area","https://ilfugiuliopascal.hopper.pw/links.html")]

#PLUGINS = ['plugins.gallery','plugins.sitemap',]
#PLUGINS = ['plugins.gallery',] no longer used

# SITEMAP = {
#     'format': 'xml',
#     'priorities': {
#         'articles': 0.5,
#         'indexes': 0.5,
#         'pages': 1
#     },
#     'changefreqs': {
#         'articles': 'monthly',
#         'indexes': 'monthly',
#         'pages': 'monthly'
#     }
# }

HIDDEN_PAGES = ['Astroparticle Physics Autumn Programme'] # The title of the index and/or other things

DATE = strftime("on %A, %d %B %Y %H:%M (%z)", localtime())

IGNORE_FILES = ['.#*','*.xcf']

FOOTER_ABOUT = "Associazione Italiana Studenti di Fisica"

FOOTER_DESCRIPTION = "The Associazione Italiana Studenti di Fisica (AISF) gathers together all the Italian students of physics. It was founded in Heidelberg in August 2014 and since January 2015 is a National Committee for the International Associazion of Physics Students (IAPS)."

# OrderedDict in this case is more useful than the default dict structure.
FOOTER_CONNECT = collections.OrderedDict([
    ('Organizing Committee','lightsoftuscany@ai-sf.it'),
    ('AISF EC','esecutivo@ai-sf.it'),
    ('IAPS EC','ec@iaps.info'),
    ('Technical support','postmaster@ai-sf.it'),
])

FOOTER_CONTACT = collections.OrderedDict([
    ('Facebook Event Page','https://www.facebook.com/events/895616630487424/'),
    ('AISF Website','http://www.ai-sf.it/joomla/it'),
    ('IAPS Website','http://www.iaps.info'),
])

MENUITEMS= [('AISF','http://ai-sf.it')]
OGURL = "http://www.ai-sf.it/apap"

NICKNAME="apap" # Prefix of the Name Page

FOOTER_COLOR = "purple darken-4"
FOOTER_COLOR_TEXT = "white"
COLOR = "purple-text text-darken-2"
