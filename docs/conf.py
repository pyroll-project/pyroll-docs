# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import json
from pathlib import Path
import sphinx_rtd_theme

ROOT_DIR = Path(__file__).parent

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'PyRolL'
copyright = '2022, The PyRolL Project'
author = 'Max Weiner, Christoph Renzing, Matthias Schmidtchen'

# The full version, including alpha/beta/rc tags
release = '2.0.0a'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "readthedocs_ext.readthedocs",
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx_rtd_theme",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

toc_object_entries = False
# nitpicky = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_logo = "img/pyroll-bird-head.svg"
html_theme_options = {
    'logo_only': True,
    'display_version': True,
    'style_nav_header_background': '#343131',
    # Toc options
    'navigation_depth': -1,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# MyST
myst_heading_anchors = 3
myst_title_to_header = True
myst_enable_extensions = [
    "dollarmath",
    "fieldlist",
    "smartquotes",
    "replacements",
]

# AutoDoc
add_module_names = False
autodoc_typehints_format = "short"
autoclass_content = "both"
autodoc_member_order = "groupwise"

# InterSphinx
intersphinx_mapping = {
    "pluggy": ("https://pluggy.readthedocs.io/en/stable", None),
    "pandas": ("https://pandas.pydata.org/docs/", None),
    "maplotlib": ("https://matplotlib.org/stable/", None),
    "shapely": ("https://shapely.readthedocs.io/en/stable/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
}

# Jinja

jinja_contexts = {
    "plugins/index": json.loads((ROOT_DIR / "plugins" / "plugins.json").read_text()),
    "extensions/index": json.loads((ROOT_DIR / "extensions" / "extensions.json").read_text())
}


def rstjinja(app, docname, source):
    """
    Render our pages as a jinja template for fancy templating goodness.
    """
    # Make sure we're outputting HTML
    if app.builder.format != 'html':
        return
    src = source[0]
    rendered = app.builder.templates.render_string(
        src, app.config.jinja_contexts.get(docname, {})
    )
    source[0] = rendered


def setup(app):
    app.add_config_value('jinja_contexts', {}, 'html')
    app.connect("source-read", rstjinja)
