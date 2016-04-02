Irrational theme
==============


What is irrational?
------------------

irrational is a visually (c)lean, responsive, configurable theme for the
`Sphinx`_ documentation system. It is Python 2+3 compatible.
Code source is published at https://lab.errorist.xyz/sphinx/irrational.

It began as a third-party theme for https://lab.errorist.xyz projects.


Features
--------

Specifically, as compared to Kenneth's theme:

* Easy ability to install/use as a Python package (tip o' the hat to `Dave &
  Eric's sphinx_rtd_theme <https://github.com/snide/sphinx_rtd_theme>`_ for
  showing the way);
* Style tweaks, such as better code-block alignment, Github button placement,
  page source link moved to footer, improved (optional) related-items sidebar
  item, etc;
* Many customization hooks, including toggle of various sidebar & footer
  components; header/link/etc color control; etc;
* Improved documentation for all customizations (pre-existing & new).


Installation
------------

The bare minimum required to install is as follows:

#. ``pip install irrational`` (or equivalent).
#. Enable the 'irrational' theme, mini-extension, and sidebar templates in your
   ``conf.py``:

   .. code-block:: python

        import irrational

        html_theme_path = [irrational.get_path()]
        extensions = ['irrational']
        html_theme = 'irrational'
        html_sidebars = {
            '**': [
                'about.html',
                'navigation.html',
                'relations.html',
                'searchbox.html',
                'donate.html',
            ]
        }

That's it! You now have the standard irrational theme set up. Read on for more
configuration options/concerns.

Theme location
--------------

The function ``irrational.get_path`` dynamically returns irrational's install
location, ensuring that Sphinx can find and load it regardless of where/how
you installed irrational. Using it is highly recommended.

If you've manually installed irrational and/or are doing funky things to your
PYTHONPATH, you may need to replace the ``irrational.get_path()`` call with your
own explicit string, as per `the Sphinx config docs
<http://sphinx-doc.org/config.html#confval-html_theme_path>`_.

Sidebars
--------

Feel free to adjust ``html_sidebars`` as desired - the theme is designed
assuming you'll always have ``about.html`` activated, but otherwise it doesn't
care much.

* See `the Sphinx docs
  <http://sphinx-doc.org/config.html#confval-html_sidebars>`_ for details on
  how this setting behaves.
* irrational provides ``about.html`` (logo, github button + blurb),
  ``donate.html`` (Gratipay blurb/button) and ``navigation.html`` (a more
  flexible version of the builtin ``localtoc``/``globaltoc`` templates).
  ``searchbox.html`` comes with Sphinx itself.

Images
------

If you're using either of the image-related options outlined below (``logo`` or
``touch-icon``), you'll also want to tell Sphinx where to get your images from.
If so, add a line like this (changing the path if necessary; see `the Sphinx
docs for 'html_static_path'
<http://sphinx-doc.org/config.html?highlight=static#confval-html_static_path>`_):

.. code-block:: python

    html_static_path = ['_static']


Theme options
-------------

irrational's primary configuration route is the ``html_theme_options`` variable,
set in ``conf.py`` alongside the rest. A brief example (*note*: snippet doesn't
include all possible options, see following list!):

.. code-block:: python

    html_theme_options = {
        'logo': 'logo.png',
        'github_user': 'bitprophet',
        'github_repo': 'irrational',
    }

Variables and feature toggles
-----------------------------

* ``logo``: Relative path (from ``$PROJECT/_static/``) to a logo image, which
  will appear in the upper left corner above the name of the project.

  * If ``logo`` is not set, your ``project`` name setting (from the top
    level Sphinx config) will be used in a text header instead. This
    preserves a link back to your homepage from inner doc pages.

* ``logo_name``: Set to ``true`` to insert your site's ``project`` name
  under the logo image as text. Useful if your logo doesn't include the
  project name itself. Defaults to ``false``.
* ``logo_text_align``: Which CSS ``text-align`` value to use for logo text
  (if there is any.)
* ``body_text_align``: Which CSS ``text-align`` value to use for body text
  (if there is any.)
* ``description``: Text blurb about your project, to appear under the logo.
* ``description_font_style``: Which CSS ``font-style`` to use for description
  text. Defaults to ``normal``.
* ``github_user``, ``github_repo``: Used by ``github_button`` and ``github_banner``
  (see below); does nothing if both of those are set to ``false``.
* ``github_button``: ``true`` or ``false`` (default: ``true``) - whether to link to
  your Github.

   * If ``true``, requires that you set ``github_user`` and ``github_repo``.
   * See also these other related options, which behave as described in
     `Github Buttons' README
     <https://github.com/mdo/github-buttons#usage>`_:

      * ``github_type``: Defaults to ``watch``.
      * ``github_count``: Defaults to ``true``.

* ``github_banner``: ``true`` or ``false`` (default: ``false``) - whether to
  apply a 'Fork me on Github' banner in the top right corner of the page.

   * If ``true``, requires that you set ``github_user`` and ``github_repo``.
   * May also submit a string file path (as with ``logo``, relative to
     ``$PROJECT/_static/``) to be used as the banner image instead of the
     default.

* ``travis_button``: ``true``, ``false`` or a Github-style ``"account/repo"``
  string - used to display a `Travis-CI <https://travis-ci.org>`_ build status
  button in the sidebar. If ``true``, uses your ``github_(user|repo)``
  settings; defaults to ``false.``
* ``codecov_button``: ``true``, ``false`` or a Github-style
  ``"account/repo"`` string - used to display a `Codecov`_
  build status button in the sidebar. If ``true``, uses your
  ``github_(user|repo)`` settings; defaults to ``false.``
* ``gratipay_user``: Set to your `Gratipay <https://gratipay.com>`_ username
  if you want a Gratipay 'Donate' section in your sidebar.

  * This used to be ``gittip_user`` before that service changed its name to
    Gratipay; we've left the old setting in place as an alias for backwards
    compatibility reasons. It may be removed in the future.
  * If both options are given, ``gratipay_user`` wins.

* ``analytics_id``: Set to your `Google Analytics
  <http://www.google.com/analytics/>`_ ID (e.g. ``UA-#######-##``) to enable
  tracking.
* ``touch_icon``: Path to an image (as with ``logo``, relative to
  ``$PROJECT/_static/``) to be used for an iOS application icon, for when
  pages are saved to an iOS device's home screen via Safari.
* ``extra_nav_links``: Dictionary mapping link names to link targets; these
  will be added in a UL below the main sidebar navigation (provided you've
  enabled ``navigation.html``.) Useful for static links outside your Sphinx
  doctree.
* ``sidebar_includehidden``: Boolean determining whether the TOC sidebar
  should include hidden Sphinx toctree elements. Defaults to ``true`` so you
  can use ``:hidden:`` in your index page's root toctree & avoid having 2x
  copies of your navigation on your landing page.
* ``show_powered_by``: Boolean controlling display of the ``Powered by
  Sphinx N.N.N. & irrational M.M.M`` section of the footer. When ``true``, is
  displayed next to the copyright information; when ``false``, is hidden.
* ``show_related``: Boolean controlling whether the 'next/previous/related'
  secondary navigation elements are hidden or displayed. Defaults to ``false``
  since on many sites these elements are superfluous.
* ``page_width``: CSS width specifier controlling default content/page width.
  Defaults to ``940px``.
* ``sidebar_width``: CSS width specifier controlling default sidebar width.
  Defaults to ``220px``.

Style colors
------------

These should be fully qualified CSS color specifiers such as ``#004B6B`` or
``#444``. The first few items in the list are "global" colors used as defaults
for many of the others; update these to make sweeping changes to the
colorscheme. The more granular settings can be used to override as needed.

* ``gray_1``: Dark gray.
* ``gray_2``: Light gray.
* ``gray_3``: Medium gray.
* ``pink_1``: Light pink.
* ``pink_2``: Medium pink.
* ``body_text``: Main content text.
* ``footer_text``: Footer text (includes links.)
* ``link``: Non-hovered body links.
* ``link_hover``: Body links, hovered.
* ``sidebar_header``: Sidebar headers. Defaults to ``gray_1``.
* ``sidebar_text``: Sidebar paragraph text.
* ``sidebar_link``: Sidebar links (there is no hover variant.) Applies to
  both header & text links. Defaults to ``gray_1``.
* ``sidebar_link_underscore``: Sidebar links' underline (technically a
  bottom-border).
* ``sidebar_search_button``: Background color of the search field's 'Go'
  button.
* ``sidebar_list``: Foreground color of sidebar list bullets & unlinked text.
* ``sidebar_hr``: Color of sidebar horizontal rule dividers. Defaults to
  ``gray_3``.
* ``anchor``: Foreground color of section anchor links (the 'paragraph'
  symbol that shows up when you mouseover page section headers.)
* ``anchor_hover_fg``: Foreground color of section anchor links (as above)
  when moused over. Defaults to ``gray_1``.
* ``anchor_hover_bg``: Background color of above.
* ``note_bg``: Background of ``.. note::`` blocks. Defaults to ``gray_2``.
* ``note_border``: Border of same.
* ``seealso_bg``: Background of ``.. seealso::`` blocks. Defaults to
  ``gray_2``.
* ``seealso_border``: Border of same.
* ``warn_bg``: Background of ``.. warn::`` blocks. Defaults to ``pink_1``.
* ``warn_border``: Border of same. Defaults to ``pink_2``.
* ``footnote_bg``: Background of footnote blocks.
* ``footnote_border``: Border of same. Defaults to ``gray_2``.
* ``pre_bg``: Background of preformatted text blocks (including code
  snippets.) Defaults to ``gray_2``.
* ``narrow_sidebar_bg``: Background of 'sidebar' when narrow window forces
  it to the bottom of the page.
* ``narrow_sidebar_fg``: Text color of same.
* ``narrow_sidebar_link``: Link color of same. Defaults to ``gray_3``.
* ``code_highlight``: Color of highlight when using ``:emphasize-lines:`` in a code block.

Fonts
-----

* ``font_family``: Font family of body text.  Defaults to ``'goudy old style',
  'minion pro', 'bell mt', Georgia, 'Hiragino Mincho Pro', serif``.
* ``head_font_family``: Font family of headings.  Defaults to ``'Garamond',
  'Georgia', serif``.
* ``code_font_size``: Font size of code block text. Defaults to ``0.9em``.
* ``code_font_family``: Font family of code block text. Defaults to
  ``'Consolas', 'Menlo', 'Deja Vu Sans Mono', 'Bitstream Vera Sans Mono',
  monospace``.


Project background
------------------

irrational is a modified version of `Jeff Forcier's
<http://bitprophet.org>`_ `"Alabaster" Sphinx theme
<https://github.com/bitprophet/alabaster>`_, based on
a modified (with permission) version of `Kenneth Reitz's
<http://kennethreitz.org>`_ `"krTheme" Sphinx theme
<https://github.com/kennethreitz/kr-sphinx-themes>`_ (it's the one used
in his `Requests <http://python-requests.org>`_ project). Kenneth's
theme was itself originally based on Armin Ronacher's `Flask
<http://flask.pocoo.org/>`_ theme. Many thanks to both for their hard work.

.. _Codecov: https://codecov.io
.. _Sphinx: http://sphinx-doc.org
