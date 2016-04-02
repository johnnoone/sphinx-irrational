#!/usr/bin/env python

import sys
import os
extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = 'Irrational'
copyright = '2016, Xavier Barbosa'
author = 'Xavier Barbosa'

from irrational._version import __version__
version = __version__
release = __version__

language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'irrational'
html_static_path = ['_static']
html_sidebars = {
    '**': []
}
html_show_sourcelink = False
html_show_sphinx = False
