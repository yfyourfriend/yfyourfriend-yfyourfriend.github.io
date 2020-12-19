#/c/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

AUTHOR = "Loh Yi Fong"
SITENAME = """<span style="color:black;">Yi</span> <span style="color:darkblue;">Fong's</span> <span style="color:#AA1032;"'s page'</span>"""
SITEURL = ""
SITESUBTITLE = "Suppose not!"

PATH = "content"

# Regional Settings
TIMEZONE = "Asia/Singapore"
DATE_FORMATS = {"en": "%b %d, %Y"}

# Plugins and extensions
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.admonition": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.sane_lists": {},
        "markdown.extensions.toc": {"permalink": " "},
    }
}
PLUGIN_PATHS = ["/home/yfyourfriend/Documents/venv/pelican/lib64/python3.8/site-packages/pelican/plugins/"]
PLUGINS = [
    "assets",
    "extract_toc",
    "liquid_tags.include_code",
    "neighbors",
    "related_posts",
    "series",
    "share_post",
    "tipue_search",
]
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

# Appearance
TYPOGRIFY = True
THEME = "elegant"
# THEME = "~/Documents/venv/pelican/lib64/python3.8/site-packages/pelican/themes/elegant"
DEFAULT_PAGINATION = False
# Defaults
DEFAULT_CATEGORY = "Miscellaneous"
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = "{slug}"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"
TAGS_URL = "tags"
CATEGORIES_URL = "categories"
ARCHIVES_URL = "archives"
SEARCH_URL = "search"

# Feeds
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None

# Social
SOCIAL = (
    ("Email", "mailto:lohyifong@gmail.com", "My Emaill Address"),
    ("Github", "https://github.com/yfyourfriend/", "My Github Profile"),
    ("Linkedin", "https://www.linkedin.com/in/yfloh/", "My Linkedin Profile")
)

"""
    ("RSS", SITEURL + "/feeds/all.atom.xml"),
    ("GoodReads", "https://www.goodreads.com/talha131"),
    ("Keybase", "https://keybase.io/talha131"),
"""

STATIC_PATHS = [
    "theme/images",
    "images",
    "extra/_redirects",
    "extra/robots.txt",
    "extra/keybase.txt",
    "code",
    "pdfs",
]
EXTRA_PATH_METADATA = {
    "extra/_redirects": {"path": "_redirects"},
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/keybase.txt": {"path": "keybase.txt"},
}

DIRECT_TEMPLATES = ("index", "tags", "categories", "archives", "search", "404")
TAG_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
USE_SHORTCUT_ICONS = True

# Elegant Labels
SOCIAL_PROFILE_LABEL = "Stay in Touch"
RELATED_POSTS_LABEL = "Keep Reading"
SHARE_POST_INTRO = "Like this post? Share on:"
COMMENTS_INTRO = """So what do you think? Did I miss something? Is any part unclear?
            Leave your comments below.
        """

# Comment System
COMMENTBOX_PROJECT = "5662225582784512-proj"


# Mailchimp
EMAIL_SUBSCRIPTION_LABEL = "Get New Posts In Your Inbox"
EMAIL_FIELD_PLACEHOLDER = "Enter your email..."
SUBSCRIBE_BUTTON_TITLE = "Subscribe Me"
MAILCHIMP_FORM_ACTION = "empty"

# SMO
TWITTER_USERNAME = ""
# TWITTER_USERNAME = "talham_"
FEATURED_IMAGE = SITEURL + "/theme/images/apple-touch-icon-152x152.png"

# Legal
SITE_LICENSE = """Content licensed under <a rel="license nofollow noopener noreferrer"
    href="http://creativecommons.org/licenses/by/4.0/" target="_blank">
    Creative Commons Attribution 4.0 International License</a>."""
HOSTED_ON = {"name": "Github Pages", "url": "https://www.github.com/"}

# SEO
SITE_DESCRIPTION = "My name is Loh Yi Fong. I am a student of mathematics and a hobbyist with computers. I like to read and gently push ideas towards the Fantastique; I try to dream, think and prove ideas. This is my personal blog."

# Landing Page
PROJECTS = [
    {
        "name": "Talks, work, courses, teaching",
        "url": "landing-page-talks-hidden.html",
        "description": "An idea of what I've worked and am working on",
    },
    {
        "name": "Resume",
        "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "description": "My resume for jobs. Currently broken link.",
    },
    {
        "name": "CV",
        "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "description": "My academic CV. Currently broken link.",
    },
"""
    {
        "name": "Papers",
        "url": "landing-page-papers-hidden.html",
        "description": "",
    },
    {
        "name": "tipue_search",
        "url": "https://github.com/getpelican/pelican-plugins/tree/master/tipue_search",
        "description": "A Pelican plugin to serialize generated HTML to a JavaScript variable that can be used by jQuery plugin - Tipue Search",
    },
    {
        "name": "share_post",
        "url": "https://github.com/getpelican/pelican-plugins/tree/master/share_post",
        "description": "A Pelican plugin to create share URLs of article",
    },
    {
        "name": "goodreads_activity",
        "url": "https://github.com/getpelican/pelican-plugins/tree/master/goodreads_activity",
        "description": "A Pelican plugin to lists books from your GoodReads shelves",
    },
    {
        "name": "TiddlyWiki",
        "url": "https://github.com/Jermolene/TiddlyWiki5/commits?author=talha131",
        "description": "My contributions to TiddlyWiki, a self-contained JavaScript wiki",
    },
    {
        "name": "Pelican Plugins",
        "url": "https://github.com/getpelican/pelican-plugins/commits?author=talha131",
        "description": "My contributions to plugins for Pelican blog engine",
    },
    {
        "name": "Pelican",
        "url": "https://github.com/getpelican/pelican/commits?author=talha131",
        "description": "Static site generator that supports Markdown and"
        " reST syntax",
    },
    {
        "name": "coc-lists",
        "url": "https://github.com/neoclide/coc-lists/commits?author=talha131",
        "description": "Common lists extension for coc.nvim",
    },
    {
        "name": "Logpad + Duration",
        "url": "https://github.com/talha131/logpad-plus-duration#logpad--duration",
        "description": "Vim plugin to emulate Windows Notepad logging feature,"
        " and log duration of each entry",
    },
    {
        "name": "Asana to Github Issues",
        "url": "https://github.com/talha131/AsanaToGithub#asana-to-github",
        "description": "Command-line program to move your tasks from Asana"
        " projects to Github issues",
    },
    {
        "name": "Asana",
        "url": "https://github.com/pandemicsyn/asana/commits?author=talha131",
        "description": "Python Asana API bindings",
    },
    {
        "name": "Ctags",
        "url": "https://github.com/fishman/ctags/commits?author=talha131",
        "description": "Exuberant Ctags clone with ObjectiveC and CSS support",
    },
    {
        "name": "Wasavi",
        "url": "https://github.com/akahuku/wasavi/commits?author=talha131",
        "description": "A browser extension that changes textarea element to"
        " Vi editor",
    },"""
]

LANDING_PAGE_TITLE = "<em>beautiful dreamer queen of my song </em>"
