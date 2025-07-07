# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Exploring Robot Reinforcement Learning Tools and Compatibilities'
copyright = '2025, Kushal Agarwal'
author = 'Kushal Agarwal'
release = '1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'myst_parser',
    "sphinx_copybutton",
    "sphinx_rtd_theme",    
]

templates_path = ['_templates']
exclude_patterns = []

# Support both .md and .rst files
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

def setup(app):
    app.add_css_file('custom.css')
    app.add_js_file('custom.js')

html_theme_options = {
    'navigation_depth': 4,  # or however deep your TOC goes
    'titles_only': False
}

numfig = True  # If you want numbered figures/tables as well
