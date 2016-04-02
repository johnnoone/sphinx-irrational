#!/usr/bin/env python

import sys
import os
extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = 'Errorist'
copyright = '2016, Xavier Barbosa'
author = 'Xavier Barbosa'

import errorist
version = errorist.__version__
release = errorist.__version__

language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'errorist'
html_static_path = ['_static']
html_sidebars = {
    '**': []
}
html_show_sourcelink = False
html_show_sphinx = False

html_context = {
    'git_repository': os.environ.get('CI_BUILD_REPO',
                                 'https://lab.errorist.xyz/py/errorist'),
}

rst_epilog = """
.. |git_repository| replace:: {git_repository}
""".format(**html_context)
