#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Toulibre"
SITENAME = u"Capitole du Libre"
#~ SITEURL = 'http://www.capitoledulibre.org/2012'
SITEURL = 'http://localhost:8000'
THEME = 'cdltheme-2012'
CSS_FILE = 'styles.css'
PLUGINS = ['pelican.plugins.html_rst_directive',]

DELETE_OUTPUT_DIRECTORY = True

ARTICLE_DIR = 'blog'
ARTICLE_EXCLUDES = ('','blog','intervenants',)
PAGE_DIR = 'pages'
PAGE_EXCLUDES = ('blog','intervenants',)
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_LANG_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'

DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (('Sponsors', '/sponsors.html'),
             ('Informations pratiques', '/informations-pratiques.html'),)
PROG_MENUITEMS = (('Capitole du Libre', '/programme-des-conferences-et-ateliers.html'),
                  ('Akademy-fr', '/akademyfr.html'),
                  ('DjangoCon', '/djangocon-toulouse.html'),
                  ('Ubuntu Party', '/ubuntu-party-toulouse-2012.html'),)
             
SOCIAL = (('twitter', 'http://twitter.com/Toulibreorg'),)

TIMEZONE = 'Europe/Paris'
DATE_FORMAT = {
    'fr': ('fr_FR','%d %b %Y'),
    'en': ('en_US','%a, %d %b %Y'),
}
DEFAULT_LANG='fr'

# Blogroll
LINKS =  (
    ('Toulibre', 'http://www.toulibre.org/'),
    ('Ubuntu-fr', 'http://www.ubuntu-fr.org/'),
         )

# Social widget
SOCIAL = (
          ('Twitter', 'https://twitter.com/toulibreorg'),
          ('Lanyrd', 'http://lanyrd.com/2012/capitole-du-libre/'),
         )

TWITTER_USERNAME = 'Toulibreorg'

DEFAULT_PAGINATION = 4


# static paths will be copied under the same name
STATIC_PATHS = ["files","logos","photos",] 
RELATIVE_URLS = False

DIRECT_TEMPLATE = ('index', 'tags', 'categories', 'archives')
