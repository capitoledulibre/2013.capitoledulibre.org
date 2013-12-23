#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Toulibre"
SITENAME = u"Capitole du Libre"
SITEURL = 'http://localhost:8000'
SITEDESCRIPTION = u'L\'événement autour de Logiciel Libre à Toulouse'
THEME = 'cdltheme-2013'
OUTPUT_PATH = 'output-cdl2013/'
CSS_FILE = 'styles.css'
PLUGIN_PATH = '../src/pelican-plugins'
PLUGINS = ['html_rst_directive','ical']

DELETE_OUTPUT_DIRECTORY = True
WITH_FUTURE_DATES = False

ARTICLE_DIR = 'blog'
ARTICLE_EXCLUDES = ('','blog','intervenants','sponsors','liens')
PAGE_DIR = 'pages'
PAGE_EXCLUDES = ('blog','intervenants',)
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}-{date:%d}-{slug}.html'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}-{date:%d}-{slug}.html'
ARTICLE_LANG_URL = 'blog/{date:%Y}/{date:%m}-{date:%d}-{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = 'blog/{date:%Y}/{date:%m}-{date:%d}-{slug}-{lang}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'

DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (('Programme', SITEURL + '/programme.html'),
             ('Sponsors', SITEURL + '/sponsors.html'),
             ('Informations pratiques', SITEURL + '/informations-pratiques.html'),
             ('Communication', SITEURL + '/communication.html'),
             ('Blog', SITEURL + '/blog.html'),)

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
          ('Identica', 'identica', 'http://identi.ca/toulibreorg'),
          ('Twitter', 'twitter', 'https://twitter.com/toulibreorg'),
          ('Google+', 'google', 'https://plus.google.com/b/109128243242581226442/109128243242581226442/posts'),
          ('Lanyrd', 'lanyrd', 'http://lanyrd.com/2013/capitole-du-libre/'),
         )

TWITTER_USERNAME = 'Toulibreorg'

DEFAULT_PAGINATION = 4
SUMMARY_MAX_LENGTH = 50

# static paths will be copied under the same name
STATIC_PATHS = ["files","logos","photos","icons",] 
RELATIVE_URLS = False

DIRECT_TEMPLATES = ('index', 'blog', 'tags', 'categories', 'archives', 'map', 'questionnaire', 'live')

TEMPLATE_PAGES = {'pages/conferences/conferences-grand-public.html': 'programme/conferences-grand-public.html',
                    'pages/conferences/conferences-techniques.html': 'programme/conferences-techniques.html',
                    'pages/conferences/conferences-internet-libre.html': 'programme/conferences-internet-libre.html',
                    'pages/conferences/conferences-multimedia-bureautique.html': 'programme/conferences-multimedia-bureautique.html',
                    'pages/conferences/conferences-akademy-fr.html': 'programme/conferences-akademy-fr.html',
                    'pages/ateliers/ateliers.html': 'programme/ateliers.html',
                    }

SCHEDULE_PAGES = [{'url': 'programme/conferences-grand-public.html','title':'Grand Public : A001'},
                    {'url': 'programme/conferences-multimedia-bureautique.html','title':'Multimedia / bureautique : A002'},
                    {'url': 'programme/conferences-internet-libre.html','title':'Internet Libre : C002'},
                    {'url': 'programme/conferences-techniques.html','title':'Technique : A201'},
                    {'url': 'programme/conferences-akademy-fr.html','title':'Akademy-fr : C103'},]

VIDEO_PAGES = [{'url': 'conferences/grand-public/','title':'Grand Public'},
                    {'url': 'conferences/multimedia-bureautique/','title':'Multimedia / bureautique'},
                    {'url': 'conferences/internet-libre/','title':'Internet Libre'},
                    {'url': 'conferences/technique/','title':'Technique'},
                    {'url': 'conferences/akademy-fr/','title':'Akademy-fr'},
                    {'url': 'conferences/francejs/','title':'FranceJS'},
                    {'url': 'conferences/lua-workshop/','title':'Lua workshop'},
                    {'url': 'conferences/openstack/','title':'OpenStack'},
                    ]
