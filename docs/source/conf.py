# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "Django Pro"
copyright = "2021, Carlos Regis"
author = "carlos-regis"

release = "0.1"
version = "0.1.0"

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    # "notfound.extension",
]

templates_path = ["_templates"]

# -- Options for EPUB output
epub_show_urls = "footnote"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output
html_theme = "sphinx_rtd_theme"
