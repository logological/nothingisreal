from __future__ import unicode_literals
import subprocess
import datetime

AUTHOR = u'Tristan Miller'
SITETITLE = u"<b>Tristan Miller</b>"
SITENAME = u"Tristan Miller"
#SITEKEYWORDS = ', '.join([
#    'natural language processing', 'nlp', 'computational linguistics', 'logology', 'free software', 'humour'
#    ])
SITEURL = ''

REPOURL = 'https://github.com/logological/logological.org'
DESCRIPTION = ""
BANNER = ""
BUILD_TIME = datetime.date.today().strftime(format='%Y-%m-%d')

# Get the current git commit hash
COMMIT = ''
process = subprocess.Popen('git rev-parse HEAD'.split(), cwd='.',
                           stdout=subprocess.PIPE)
git_hash = process.communicate()[0].strip().decode('utf-8')
if git_hash:
    COMMIT = ' (<a href="{url}/commit/{commit}">{commit_link}</a>)'.format(
            url=REPOURL, commit=git_hash, commit_link=git_hash[:7])

# Language and time
DEFAULT_DATE = 'fs'
DEFAULT_LANG = u'en-ca'
TIMEZONE = u'Europe/Berlin'

# This goes at the footer of the site
FOOTER_LEFT = "" # Superseded; see base.html
FOOTER_RIGHT = """
<a href="/credits.html">Credits</a> &bullet;
<a href="{repo}">Source</a>
""".format(date=BUILD_TIME, commit=COMMIT, repo=REPOURL, repo_name=REPOURL[8:])

# Where to put generated files
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
USE_FOLDER_AS_CATEGORY = True
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'

STATIC_PATHS = [
    'images',
    'extra/apple-touch-icon-114x114.png',
    'extra/apple-touch-icon-120x120.png',
    'extra/apple-touch-icon-144x144.png',
    'extra/apple-touch-icon-152x152.png',
    'extra/apple-touch-icon-57x57.png',
    'extra/apple-touch-icon-60x60.png',
    'extra/apple-touch-icon-72x72.png',
    'extra/apple-touch-icon-76x76.png',
    'extra/favicon-128.png',
    'extra/favicon-16x16.png',
    'extra/favicon-196x196.png',
    'extra/favicon-32x32.png',
    'extra/favicon-96x96.png',
    'extra/favicon.ico',
    'extra/favicon.png',
    'extra/favicon.svg',
    'extra/mstile-144x144.png',
    'extra/mstile-150x150.png',
    'extra/mstile-310x150.png',
    'extra/mstile-310x310.png',
    'extra/mstile-70x70.png',
    'extra/EFBF4915.txt',
    'extra/BF8A2EE4.txt',
]
EXTRA_PATH_METADATA = {
    'extra/apple-touch-icon-114x114.png': {'path': 'apple-touch-icon-114x114.png'},
    'extra/apple-touch-icon-120x120.png': {'path': 'apple-touch-icon-120x120.png'},
    'extra/apple-touch-icon-144x144.png': {'path': 'apple-touch-icon-144x144.png'},
    'extra/apple-touch-icon-152x152.png': {'path': 'apple-touch-icon-152x152.png'},
    'extra/apple-touch-icon-57x57.png': {'path': 'apple-touch-icon-57x57.png'},
    'extra/apple-touch-icon-60x60.png': {'path': 'apple-touch-icon-60x60.png'},
    'extra/apple-touch-icon-72x72.png': {'path': 'apple-touch-icon-72x72.png'},
    'extra/apple-touch-icon-76x76.png': {'path': 'apple-touch-icon-76x76.png'},
    'extra/favicon-128.png': {'path': 'favicon-128.png'},
    'extra/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extra/favicon-196x196.png': {'path': 'favicon-196x196.png'},
    'extra/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extra/favicon-96x96.png': {'path': 'favicon-96x96.png'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/favicon.png': {'path': 'favicon.png'},
    'extra/favicon.svg': {'path': 'favicon.svg'},
    'extra/mstile-144x144.png': {'path': 'mstile-144x144.png'},
    'extra/mstile-150x150.png': {'path': 'mstile-150x150.png'},
    'extra/mstile-310x150.png': {'path': 'mstile-310x150.png'},
    'extra/mstile-310x310.png': {'path': 'mstile-310x310.png'},
    'extra/mstile-70x70.png': {'path': 'mstile-70x70.png'},
    'extra/EFBF4915.txt': {'path': 'EFBF4915.txt'},
    'extra/BF8A2EE4.txt': {'path': 'BF8A2EE4.txt'},
}

#READERS = {"html": None}

ARTICLES_FRONT_PAGE = 2
SUMMARY_MAX_LENGTH = 25
DEFAULT_PAGINATION = False
DISPLAY_CATEGORIES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'theme'

# Top menu
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [
    ('Publications', '/publications.html'),
    ('Software', '/software.html'),
    ('Teaching', '/teaching.html'),
    ('CV', '/miller_cv.pdf'),
    #('Activities', '/activities.html'),
    ('Fun', '/fun.html'),
    ('Miscellany', '/misc.html'),
]

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['render_math',
           'sitemap']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5},
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'weekly',
        'pages': 'weekly'}
}

#RESPONSIVE_IMAGES = False
#FIGURE_NUMBERS = True
DIRECT_TEMPLATES = ['index']
