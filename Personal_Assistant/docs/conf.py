# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import django

sys.path.append(os.path.abspath(".."))
os.environ["DJANGO_SETTINGS_MODULE"] = "Personal_Assistant.settings"
django.setup()

project = "Personal assistant"
copyright = (
    "2023, Vitalii Kiriienko, Constantine Zagorodnyi, Egor Shanin, Denys Kotsiuba"
)
author = "Vitalii Kiriienko, Constantine Zagorodnyi, Egor Shanin, Denys Kotsiuba"
release = "1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
