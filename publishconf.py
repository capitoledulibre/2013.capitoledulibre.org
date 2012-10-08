#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
sys.path.append('.')
from pelicanconf import *

SITEURL = 'http://www.capitoledulibre.org/2012'

MENUITEMS = (('Sponsors', SITEURL + '/sponsors.html'),
             ('Informations pratiques', SITEURL + '/informations-pratiques.html'),)
PROG_MENUITEMS = ((u'Conférences et ateliers du Capitole du Libre', SITEURL + '/programme-des-conferences-et-ateliers.html'),
                  (u'Akademy-fr', SITEURL + '/akademy-fr.html'),
                  (u'DjangoCon', SITEURL + '/djangocon-toulouse.html'),
                  (u'Ubuntu Party', SITEURL + '/ubuntu-party-toulouse-2012.html'),)

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# Uncomment following line for absolute URLs in production:
#RELATIVE_URLS = False

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
