#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'COMPRES Technology Office'
SITENAME = u'COMPTECH'
SITEURL = ''

TIMEZONE = 'US/Central'

DEFAULT_LANG = u'en'

PATH = 'content'

THEME = 'themes/comptech'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# newsroll
LINKS = (('Pelican', 'http://getpelican.com/'),
        ('Python.org', 'http://python.org/'),
        ('Jinja2', 'http://jinja.pocoo.org/'),
        ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# Plugins
PLUGIN_PATH = 'plugins'
#PLUGINS = ['sitemap', 'tipue_search', 'multi_part', 'latex', 'jcpds']
PLUGINS = ['sitemap', 'multi_part', 'latex', 'jcpds', 'tipue_search']
#PUBLICATIONS_SRC = 'content/publications/pubs.bib'

#DIRECT_TEMPLATES = ('news', 'publications')
#PAGINATED_DIRECT_TEMPLATES = ('index', 'news')

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

DEFAULT_PAGINATION = 10
USE_FOLDER_AS_CATEGORY = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

ARTICLE_DIR = 'news'
ARTICLE_EXCLUDES = ('pages', 'tools',)
ARTICLE_URL = '{category}/{date:%Y}/{date:%b}-{date:%d}-{slug}.html'
ARTICLE_SAVE_AS = '{category}/{date:%Y}/{date:%b}-{date:%d}-{slug}.html'
#ARTICLE_URL = '{category}/{slug}.html'
#ARTICLE_SAVE_AS = '{category}/{slug}.html'


PAGE_DIR = ''
PAGE_EXCLUDES = ('news',)
PAGE_URL = '{category}/{slug}.html'
PAGE_SAVE_AS = '{category}/{slug}.html'

AUTHOR_SAVE_AS = False

CATEGORY_SAVE_AS = 'category/{slug}.html'
CATEGORY_URL = 'category/{slug}.html'

TAG_SAVE_AS = 'news/tag/{slug}.html'
TAG_URL = 'news/tag/{slug}.html'

DIRECT_TEMPLATES = ('index', 'news/tags', 'news/categories',
                    'news/archives', 'news/index', 'search',
                    '404')
PAGINATED_DIRECT_TEMPLATES = ('index', 'news/index')

# "static" files
STATIC_PATHS = ['CNAME', 'tools/jcpds/']

MENUITEMS = (('Home', SITEURL + '/'),
             ('About', SITEURL + '/about/'),
             ('News', SITEURL + '/news/'),
             ('Facilities', SITEURL + '/facilities/'),
             ('Tools', SITEURL + '/tools/'),
             ('Links', SITEURL + '/links/'),
             ('Contact', SITEURL + '/contact.html'))

GOOGLE_ANALYTICS = "UA-40018589-1"
