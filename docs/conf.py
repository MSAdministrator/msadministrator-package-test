"""Sphinx configuration."""
project = "Msadministrator Package Test"
author = "Josh Rickard"
copyright = "2022, Josh Rickard"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
