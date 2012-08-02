#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"numahell"
SITENAME = u"Capitole du Libre"
SITEURL = '/'
THEME = 'cdltheme-2012'
CSS_FILE = 'styles.css'

#~ 
#~ ARTICLE_DIR = 'blog'
#~ ARTICLE_EXCLUDES = ('','blog',)
#~ PAGE_DIR = ''
#~ PAGE_EXCLUDES = ('blog',)
#~ ARTICLE_URL = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}.html'
#~ ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}.html'
#~ ARTICLE_LANG_URL = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}-{lang}.html'
#~ ARTICLE_LANG_SAVE_AS = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}-{lang}.html'
#~ PAGE_URL = '{slug}.html'
#~ PAGE_SAVE_AS = '{slug}.html'
#~ PAGE_LANG_URL = '{slug}-{lang}.html'
#~ PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'

TIMEZONE = 'Europe/Paris'
DATE_FORMAT = {
    'fr': ('fr_FR','%d %b %Y'),
    'en': ('en_US','%a, %d %b %Y'),
}
DEFAULT_LANG='fr'

# Blogroll
LINKS =  (
    ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
    ('Python.org', 'http://python.org'),
    ('Jinja2', 'http://jinja.pocoo.org'),
         )

# Social widget
SOCIAL = (
          ('You can add links in your config file', '#'),
         )

DEFAULT_PAGINATION = 4


# static paths will be copied under the same name
STATIC_PATHS = ["files","logos",] 
