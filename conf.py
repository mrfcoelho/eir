# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os

project = 'EIR'
copyright = '2024, buildingSMART Portugal'
author = 'buildingSMART Portugal'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['linuxdoc.rstFlatTable']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'pt_PT'
locale_dirs = ['locale/']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    'display_version': False
}

build_all_docs = os.environ.get("build_all_docs")
pages_root = os.environ.get("pages_root", "")
current_language = os.environ.get("current_language")

if build_all_docs is not None:

  html_context = {
    'current_language' : current_language,
    'languages': [["pt", pages_root], ['en', pages_root+'/en']]
  }