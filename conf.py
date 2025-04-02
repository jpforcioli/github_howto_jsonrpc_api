# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import time


# -- Project information -----------------------------------------------------

project = 'FortiManager API HOW-TO'
copyright = '2025'
author = 'Jean-Pierre Forcioli'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#extensions = [
#    "sphinx_rtd_theme",
#]


extensions = [ 
    "sphinx_tabs.tabs",
    'sphinx_toolbox.collapse',
    'sphinx.ext.autosectionlabel',    
    'sphinxcontrib.images',    
    'sphinx_copybutton',
    "sphinx_design",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.gitignore', '.venv']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"

# Configuration for the sphinxcontrib.images extension
images_config = {
    "backend": "LightBox2",
#    "default_show_title": True,
    "default_image_width": "50%",
    "default_image_height": "50%",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
DOC_LOGO = "fortimanager_api_howto.png"
html_static_path = ['_static']
html_theme_options = {
    "announcement": "FortiManager API HOW-TO",
    "logo": {
#        "image_light": "_static/light-fortinet-logo.png",
#        "image_dark": "_static/dark-fortinet-logo.png",
        "image_light": f"_static/{DOC_LOGO}",
        "image_dark": f"_static/{DOC_LOGO}",
    },
    "show_toc_level": 5,
    "show_nav_level": 5,
    "navigation_with_keys": False,
}

version = time.ctime()
html_title = f"How to FortiManager API - {version}"

rst_prolog = """
.. |bulb| unicode:: U+1F4A1
.. |warning| unicode:: U+26A0
.. |action| unicode:: U+1F3AC
.. |clap| unicode:: U+1F44F
.. |fmg_api| replace:: FortiManager JSON RPC API
.. |json_rpc_m| replace:: JSON RPC *method*
.. |json_rpc_u| replace:: JSON RPC *url*
"""
